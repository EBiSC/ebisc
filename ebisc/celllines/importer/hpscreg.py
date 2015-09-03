import re
import functools
import requests

from ebisc.celllines.models import *

from django.conf import settings
from django.db import IntegrityError

import logging
logger = logging.getLogger('management.commands')
import pdb

'''
hPSCreg JSON data API importer.
'''


# -----------------------------------------------------------------------------
#  Run

def run():

    cellline_ids = request_get(settings.HPSCREG['list_url'])

    if cellline_ids is None:
        return

    for cellline_id in cellline_ids:
        logger.info('Fetching data for cell line %s' % cellline_id)
        json = request_get(settings.HPSCREG['cellline_url'] + cellline_id)

        if json is None:
            continue
        elif type(json) is unicode:
            logger.warn('Invalid cellline data: %s' % json)
        else:
            import_cellline(json)


# -----------------------------------------------------------------------------
# Make an API request and return JSON

def request_get(url):

    r = requests.get(url, auth=(settings.HPSCREG['username'], settings.HPSCREG['password']))

    if r.status_code != requests.codes.ok:
        logger.error('Can\' connect to the hPSGreg API (%s): %s' % (url, r.status_code))
        return None
    else:
        return r.json()


# -----------------------------------------------------------------------------
# Import cell line

def import_cellline(source):

    valuef = functools.partial(value_of_json, source)

    logger.info('Importing cell line %s' % valuef('name'))

    cell_line = Cellline(
        biosamples_id=valuef('biosamples_id'),
        hescreg_id=valuef('id'),
        name=valuef('name'),
        primary_disease=parse_disease(source),
        alternative_names=', '.join(valuef('alternate_name')) if valuef('alternate_name') is not None else '',
        donor=parse_donor(source),
        donor_age=valuef('donor_age', 'age_range'),
        derivation_country=term_list_value_of_json(source, 'derivation_country', Country),
    )

    # Organizations

    organizations = []

    for org in valuef('providers'):
        organization, role = parse_organization(org)

        if role == 'generator':
            cell_line.generator = organization
        elif role == 'owner':
            cell_line.owner = organization
        else:
            organizations.append((organization, role))

    try:
        cell_line.save()
    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

    for organization, organization_role in organizations:

        cell_line_organization, created = CelllineOrganization.objects.get_or_create(
            cell_line=cell_line,
            organization=organization,
            cell_line_org_type=organization_role,
        )
        if created:
            logger.info('Added organization %s as %s' % (organization, organization_role))

    # Vector

    if valuef('vector_type') == 'integrating':
        parse_integrating_vector(source, cell_line)

    if valuef('vector_type') == 'non_integrating':
        parse_non_integrating_vector(source, cell_line)

    parse_legal(source, cell_line)
    parse_derivation(source, cell_line)
    parse_culture_conditions(source, cell_line)
    parse_karyotyping(source, cell_line)
    parse_publications(source, cell_line)
    parse_characterization(source, cell_line)
    parse_characterization_markers(source, cell_line)

    cell_line.save()


# -----------------------------------------------------------------------------
# Convert JSON values to python values

def value_of_json(source, field, cast=None):

    if cast == 'bool':

        if source.get(field, None) == '1':
            return True
        else:
            return False

    elif cast == 'nullbool':

        if source.get(field, None) == '1':
            return True
        elif source.get(field, None) == '0':
            return False
        else:
            return None

    elif cast == 'int':

        try:
            return int(source[field])
        except KeyError:
            pass
        except:
            logger.warn('Invalid field value for int: %s=%s' % (field, source.get(field)))

        return None

    elif cast == 'gender':

        try:
            return Gender.objects.get(name=source[field])
        except KeyError:
            pass
        except Gender.DoesNotExist:
            logger.warn('Invalid donor gender: %s' % source.get(field))

        return None

    elif cast == 'age_range':

        try:
            value = source[field]
            if value == '---':
                return None
            return AgeRange.objects.get(name=value)
        except KeyError:
            pass
        except AgeRange.DoesNotExist:
            logger.warn('Invalid age range: %s' % source.get(field))

        return None

    else:
        value = source.get(field, None)

        if isinstance(value, str) or isinstance(value, unicode):
            return value.strip()
        else:
            return value


def term_list_value_of_json(source, source_field, model, model_field='name'):

    if source_field not in source:
        return None

    return term_list_value(source[source_field], model, model_field)


def term_list_value(value, model, model_field='name'):

    if value is None:
        return None

    kwargs = {}
    kwargs[model_field] = value

    value, created = model.objects.get_or_create(**kwargs)

    return value


# -----------------------------------------------------------------------------
# Specific parsers

def inject_valuef(func):
    def wrapper(source, *args):
        args = [functools.partial(value_of_json, source), source] + list(args)
        return func(*args)
    return wrapper


@inject_valuef
def parse_disease(valuef, source):

    if not valuef('disease_flag', 'bool'):
        disease = None
    else:
        try:
            disease, created = Disease.objects.get_or_create(
                icdcode=valuef('disease_doid'),
                disease=valuef('disease_doid_name'),
            )
        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            return None

        if created:
            logger.info('Found new disease: %s' % disease)

        if valuef('disease_doid_synonyms') is not None:
            synonyms = ', '.join([s.split('EXACT')[0].strip() for s in valuef('disease_doid_synonyms').split(',')])
            if synonyms != '':
                disease.synonyms = synonyms
                disease.save()

    return disease


@inject_valuef
def parse_cell_type(valuef, source):

    value = valuef('primary_celltype_name')

    if value is None:
        return

    cell_type, created = CellType.objects.get_or_create(
        name=value,
    )

    if created:
        logger.info('Found new cell type: %s' % cell_type)

    return cell_type


@inject_valuef
def parse_organization(valuef, source):

    # Organization

    organization, created = Organization.objects.get_or_create(
        name=valuef('name')
    )
    if created:
        logger.info('Found new organization: %s' % organization)

    if valuef('role') == 'Generator':

        return (organization, 'generator')

    elif valuef('role') == 'Owner':

        return (organization, 'owner')

    else:

        # Other organization roles

        organization_role, created = CelllineOrgType.objects.get_or_create(
            cell_line_org_type=valuef('role')
        )
        if created:
            logger.info('Found new organization type: %s' % organization_role)

        # Cell line organization

        return (organization, organization_role)


@inject_valuef
def parse_donor(valuef, source):

    # gender = valuef('gender_primary_cell', 'gender')

    gender = term_list_value_of_json(source, 'gender_primary_cell', Gender)

    try:
        donor = Donor.objects.get(biosamples_id=valuef('biosamples_donor_id'))

        if donor.gender != gender:
            logger.warn('Changing donor gender from %s to %s' % (donor.gender, gender))
            donor.gender = gender

    except Donor.DoesNotExist:
        donor = Donor(
            biosamples_id=valuef('biosamples_donor_id'),
            provider_donor_ids=valuef('internal_donor_ids'),
            gender=gender,
            country_of_origin=term_list_value_of_json(source, 'donor_country_origin', Country),
            ethnicity=valuef('ethnicity'),
            phenotypes=valuef('donor_phenotypes'),
        )

    try:
        donor.save()
    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

    return donor


@inject_valuef
def parse_legal(valuef, source, cell_line):

    cell_line_ethics = CelllineEthics(
        cell_line=cell_line,
        donor_consent=valuef('hips_consent_obtained_from_donor_of_tissue_flag', 'nullbool'),
        no_pressure_statement=valuef('hips_no_pressure_stat_flag', 'nullbool'),
        no_inducement_statement=valuef('hips_no_inducement_stat_flag', 'nullbool'),
        donor_consent_form=valuef('hips_informed_consent_flag', 'nullbool'),
        known_location_of_consent_form=valuef('hips_holding_original_donor_consent_flag', 'nullbool'),
        copy_of_consent_form_obtainable=valuef('hips_holding_original_donor_consent_copy_of_existing_flag', 'nullbool'),
        obtain_new_consent_form=valuef('hips_arrange_obtain_new_consent_form_flag', 'nullbool'),
        donor_recontact_agreement=valuef('hips_donor_recontact_agreement_flag', 'nullbool'),
        consent_anticipates_donor_notification_research_results=valuef('hips_consent_anticipates_donor_notification_research_results_flag', 'nullbool'),
        donor_expects_notification_health_implications=valuef('hips_donor_expects_notification_health_implications_flag', 'nullbool'),
        copy_of_donor_consent_information_english_obtainable=valuef('hips_provide_copy_of_donor_consent_information_english_flag', 'nullbool'),
        copy_of_donor_consent_form_english_obtainable=valuef('hips_provide_copy_of_donor_consent_english_flag', 'nullbool'),

        consent_permits_ips_derivation=valuef('hips_consent_permits_ips_derivation_flag', 'nullbool'),
        consent_pertains_specific_research_project=valuef('hips_consent_pertains_specific_research_project_flag', 'nullbool'),
        consent_permits_future_research=valuef('hips_consent_permits_future_research_flag', 'nullbool'),
        future_research_permitted_specified_areas=valuef('hips_future_research_permitted_specified_areas_flag', 'nullbool'),
        future_research_permitted_areas=valuef('hips_future_research_permitted_areas'),
        consent_permits_clinical_treatment=valuef('hips_consent_permits_clinical_treatment_flag', 'nullbool'),
        formal_permission_for_distribution=valuef('hips_formal_permission_for_distribution_flag', 'nullbool'),
        consent_permits_research_by_academic_institution=valuef('hips_consent_permits_research_by_academic_institution_flag', 'nullbool'),
        consent_permits_research_by_org=valuef('hips_consent_permits_research_by_org_flag', 'nullbool'),
        consent_permits_research_by_non_profit_company=valuef('hips_consent_permits_research_by_non_profit_company_flag', 'nullbool'),
        consent_permits_research_by_for_profit_company=valuef('hips_consent_permits_research_by_for_profit_company_flag', 'nullbool'),
        consent_permits_development_of_commercial_products=valuef('hips_consent_permits_development_of_commercial_products_flag', 'nullbool'),
        consent_expressly_prevents_commercial_development=valuef('hips_consent_expressly_prevents_commercial_development_flag', 'nullbool'),
        consent_expressly_prevents_financial_gain=valuef('hips_consent_expressly_prevents_financial_gain_flag', 'nullbool'),
        further_constraints_on_use=valuef('hips_further_constraints_on_use_flag', 'nullbool'),
        further_constraints_on_use_desc=valuef('hips_further_constraints_on_use'),

        consent_expressly_permits_indefinite_storage=valuef('hips_consent_expressly_permits_indefinite_storage_flag', 'nullbool'),
        consent_prevents_availiability_to_worldwide_research=valuef('hips_consent_prevents_availiability_to_worldwide_research_flag', 'nullbool'),

        consent_permits_genetic_testing=valuef('hips_consent_permits_genetic_testing_flag', 'nullbool'),
        consent_permits_testing_microbiological_agents_pathogens=valuef('hips_consent_permits_testing_microbiological_agents_pathogens_flag', 'nullbool'),
        derived_information_influence_personal_future_treatment=valuef('hips_derived_information_influence_personal_future_treatment_flag', 'nullbool'),

        donor_data_protection_informed=valuef('hips_donor_data_protection_informed_flag', 'nullbool'),
        donated_material_code=valuef('hips_donated_material_code_flag', 'nullbool'),
        donated_material_rendered_unidentifiable=valuef('hips_donated_material_rendered_unidentifiable_flag', 'nullbool'),
        genetic_information_exists=valuef('genetic_information_associated_flag', 'nullbool'),
        genetic_information_access_policy=valuef('hips_genetic_information_access_policy'),
        genetic_information_available=valuef('genetic_information_available_flag', 'nullbool'),

        consent_permits_access_medical_records=valuef('hips_consent_permits_access_medical_records_flag', 'nullbool'),
        consent_permits_access_other_clinical_source=valuef('hips_consent_permits_access_other_clinical_source_flag', 'nullbool'),
        medical_records_access_consented=valuef('hips_medical_records_access_consented_flag', 'nullbool'),
        medical_records_access_consented_organisation_name=valuef('hips_medical_records_access_consented_organisation_name'),

        consent_permits_stop_of_derived_material_use=valuef('hips_consent_permits_stop_of_derived_material_use_flag', 'nullbool'),
        consent_permits_stop_of_delivery_of_information_and_data=valuef('hips_consent_permits_delivery_of_information_and_data_flag', 'nullbool'),

        authority_approval=valuef('hips_approval_flag', 'nullbool'),
        approval_authority_name=valuef('hips_approval_auth_name'),
        approval_number=valuef('hips_approval_number'),
        ethics_review_panel_opinion_relation_consent_form=valuef('hips_ethics_review_panel_opinion_relation_consent_form_flag', 'nullbool'),
        ethics_review_panel_opinion_project_proposed_use=valuef('hips_ethics_review_panel_opinion_project_proposed_use_flag', 'nullbool'),

        recombined_dna_vectors_supplier=valuef('hips_recombined_dna_vectors_supplier'),
        use_or_distribution_constraints=valuef('hips_use_or_distribution_constraints_flag', 'nullbool'),
        use_or_distribution_constraints_desc=valuef('hips_use_or_distribution_constraints'),
        third_party_obligations=valuef('hips_third_party_obligations_flag', 'nullbool'),
        third_party_obligations_desc=valuef('hips_third_party_obligations'),
    )

    logger.info('Added cell line ethics: %s' % cell_line_ethics)

    cell_line_ethics.save()


@inject_valuef
def parse_integrating_vector(valuef, source, cell_line):

    if valuef('integrating_vector') == 'other':
        if valuef('integrating_vector_other') is not None:
            vector_name = valuef('integrating_vector_other')
        else:
            vector_name = u'Other'
    else:
        vector_name = valuef('integrating_vector')

    vector, created = IntegratingVector.objects.get_or_create(name=vector_name)

    if created:
        logger.info('Added integrating vector: %s' % vector)

    cell_line_vector = CelllineIntegratingVector(
        cell_line=cell_line,
        vector=vector,
        virus=term_list_value_of_json(source, 'integrating_vector_virus_type', Virus),
        transposon=term_list_value_of_json(source, 'integrating_vector_transposon_type', Transposon),
        excisable=valuef('excisable_vector_flag', 'bool'),
        absence_reprogramming_vectors=valuef('reprogramming_vectors_absence_flag', 'bool'),
    )

    cell_line_vector.save()

    for gene in [parse_molecule(g) for g in source.get('integrating_vector_gene_list', [])]:
        logger.info('Added gene: %s' % gene)
        cell_line_vector.genes.add(gene)

    logger.info('Added integrating vector: %s to cell line %s' % (vector, cell_line))


def parse_molecule(molecule_string):

    (catalog_id, name, catalog, kind) = re.split(r'###', molecule_string)

    return get_or_create_molecule(name, kind, catalog, catalog_id)


class InvalidMoleculeDataException(Exception):
    pass


def get_or_create_molecule(name, kind, catalog, catalog_id):

    kind_map = {
        'id_type_gene': 'gene',
        'id_type_protein': 'protein'
    }

    catalog_map = {
        'entrez_id': 'entrez',
        'ensembl_id': 'ensembl'
    }

    name = name.strip()
    name = name if name else None

    if name is None:
        logger.warn('Missing molecule name')
        raise InvalidMoleculeDataException

    try:
        kind = kind_map[kind]
    except KeyError:
        logger.warn('Invalid molecule kind: %s' % kind)
        raise InvalidMoleculeDataException

    if catalog is not None:
        try:
            catalog = catalog_map[catalog]
        except KeyError:
            logger.warn('Invalid molecule catalog: %s' % catalog)
            raise InvalidMoleculeDataException

    molecule, created = Molecule.objects.get_or_create(name=name, kind=kind)

    if created:
        logger.info('Created new molecule: %s' % molecule)

    if catalog and catalog_id:
        reference, created = MoleculeReference.objects.get_or_create(molecule=molecule, catalog=catalog, catalog_id=catalog_id)
        if created:
            logger.info('Created new molecule reference: %s' % reference)

    return molecule


@inject_valuef
def parse_non_integrating_vector(valuef, source, cell_line):

    if valuef('non_integrating_vector') == 'other':
        if valuef('non_integrating_vector_other') is not None:
            vector_name = valuef('non_integrating_vector_other')
        else:
            vector_name = u'Other'
    else:
        vector_name = valuef('non_integrating_vector')

    vector, created = NonIntegratingVector.objects.get_or_create(name=vector_name)

    if created:
        logger.info('Added non-integrating vector: %s' % vector)

    cell_line_vector = CelllineNonIntegratingVector(
        cell_line=cell_line,
        vector=vector,
    )

    cell_line_vector.save()

    for gene in [parse_molecule(g) for g in source.get('non_integrating_vector_gene_list', [])]:
        logger.info('Added gene: %s' % gene)
        cell_line_vector.genes.add(gene)

    logger.info('Added non-integrationg vector %s to cell line %s' % (vector, cell_line))


@inject_valuef
def parse_derivation(valuef, source, cell_line):

    cell_line_derivation = CelllineDerivation(
        cell_line=cell_line,
        primary_cell_type=parse_cell_type(source),
        primary_cell_developmental_stage=term_list_value_of_json(source, 'dev_stage_primary_cell', PrimaryCellDevelopmentalStage),
        reprogramming_passage_number=valuef('passage_number_reprogrammed'),
        selection_criteria_for_clones=valuef('selection_of_clones'),
        xeno_free_conditions=valuef('derivation_xeno_graft_free_flag', 'bool'),
        derived_under_gmp=valuef('derivation_gmp_ips_flag', 'bool'),
        available_as_clinical_grade=valuef('available_clinical_grade_ips_flag', 'bool'),
    )

    try:
        cell_line_derivation.save()
    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

    logger.info('Added cell line derivation: %s' % cell_line_derivation)


@inject_valuef
def parse_culture_conditions(valuef, source, cell_line):

    cell_line_culture_conditions = CelllineCultureConditions(
        cell_line=cell_line,

        surface_coating=term_list_value_of_json(source, 'surface_coating', SurfaceCoating),

        feeder_cell_id=valuef('feeder_cells_ont_id'),
        feeder_cell_type=valuef('feeder_cells_name'),

        passage_method=term_list_value_of_json(source, 'passage_method', PassageMethod),
        enzymatically=term_list_value_of_json(source, 'passage_method_enzymatically', Enzymatically),
        enzyme_free=term_list_value_of_json(source, 'passage_method_enzyme_free', EnzymeFree),

        o2_concentration=valuef('o2_concentration', 'int'),
        co2_concentration=valuef('co2_concentration', 'int'),
    )

    cell_line_culture_conditions.save()

    # Culture medium

    def parse_supplements(cell_line_culture_conditions, supplements):

        if supplements is None:
            return

        else:
            for supplement in supplements:
                (supplement, amount, unit) = supplement.split('###')
                CelllineCultureMediumSupplement(
                    cell_line_culture_conditions=cell_line_culture_conditions,
                    supplement=supplement,
                    amount=amount,
                    unit=term_list_value(unit, Unit),
                ).save()

    if not valuef('culture_conditions_medium_culture_medium') == 'other_medium':
        cell_line_culture_conditions.culture_medium = term_list_value_of_json(source, 'culture_conditions_medium_culture_medium', CultureMedium)

        # Culture medium supplements
        parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_supplements'))

    else:
        CultureMediumOther(
            cell_line_culture_conditions=cell_line_culture_conditions,
            base=valuef('culture_conditions_medium_culture_medium_other_base'),
            protein_source=term_list_value_of_json(source, 'culture_conditions_medium_culture_medium_other_protein_source', ProteinSource),
            serum_concentration=valuef('culture_conditions_medium_culture_medium_other_concentration', 'int'),
        ).save()

        # Culture medium supplements
        parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_other_supplements'))

    # Final save

    cell_line_culture_conditions.save()
    logger.info('Added cell line culture conditions: %s' % cell_line_culture_conditions)


@inject_valuef
def parse_karyotyping(valuef, source, cell_line):

    if valuef('karyotyping_flag', 'bool'):

        cell_line_karyotype = CellLineKaryotype(
            cell_line=cell_line,
            karyotype=valuef('karyotyping_karyotype'),
            karyotype_method=term_list_value_of_json(source, 'karyotyping_method', KaryotypeMethod),
            passage_number=valuef('karyotyping_number_passages'),
        )

        cell_line_karyotype.save()

        logger.info('Added cell line karyotype: %s' % cell_line_karyotype)


@inject_valuef
def parse_publications(valuef, source, cell_line):

    if valuef('registration_reference_publication_pubmed_id', 'int'):
        # PubMed
        CelllinePublication(
            cell_line=cell_line,
            reference_type='pubmed',
            reference_id=valuef('registration_reference_publication_pubmed_id', 'int'),
            reference_url=CelllinePublication.pubmed_url_from_id(valuef('registration_reference_publication_pubmed_id', 'int')),
            reference_title=valuef('registration_reference'),
        ).save()


@inject_valuef
def parse_characterization(valuef, source, cell_line):

    certificate_of_analysis_passage_number = valuef('certificate_of_analysis_passage_number')
    screening_hiv1 = valuef('virology_screening_hiv_1_result')
    screening_hiv2 = valuef('virology_screening_hiv_2_result')
    screening_hepatitis_b = valuef('virology_screening_hbv_result')
    screening_hepatitis_c = valuef('virology_screening_hcv_result')
    screening_mycoplasma = valuef('virology_screening_mycoplasma_result')

    if len([x for x in (certificate_of_analysis_passage_number, screening_hiv1, screening_hiv2, screening_hepatitis_b, screening_hepatitis_c, screening_mycoplasma) if x is not None]):
        CelllineCharacterization(
            cell_line=cell_line,
            certificate_of_analysis_passage_number=certificate_of_analysis_passage_number,
            screening_hiv1=screening_hiv1,
            screening_hiv2=screening_hiv2,
            screening_hepatitis_b=screening_hepatitis_b,
            screening_hepatitis_c=screening_hepatitis_c,
            screening_mycoplasma=screening_mycoplasma,
        ).save()


@inject_valuef
def parse_characterization_markers(valuef, source, cell_line):

    def aux_hescreg_data_url(filename):
        if filename is None:
            return None
        else:
            # TODO: add url prefix
            return '%s' % valuef('undiff_morphology_markers_enc_filename')

    def aux_imune_rtpcr_facs(hescreg_slug, hescreg_slug_passage_number, marker_model, marker_molecule_model):

        if valuef(hescreg_slug) is not None:
            marker = marker_model(
                cell_line=cell_line,
                passage_number=valuef(hescreg_slug_passage_number)
            )
            marker.save()

            for string in valuef(hescreg_slug):
                aux_molecule_result(marker, marker_molecule_model, string)

    def aux_molecule_result(marker, marker_molecule_model, string):

        if len(string.split('###')) == 2:
            # TODO
            pass
        else:
            (molecule_catalog_id, result, molecule_name, molecule_catalog, molecule_kind) = string.split('###')
            try:
                molecule = get_or_create_molecule(molecule_name, molecule_kind, molecule_catalog, molecule_catalog_id)
                marker_molecule_model(
                    marker=marker,
                    molecule=molecule,
                    result=result).save()
            except InvalidMoleculeDataException:
                pass

    # UndifferentiatedMorphologyMarkerImune, UndifferentiatedMorphologyMarkerRtPcr, UndifferentiatedMorphologyMarkerFacs

    undiff_types = (
        ('undiff_immstain_marker', 'undiff_immstain_marker_passage_number', UndifferentiatedMorphologyMarkerImune, UndifferentiatedMorphologyMarkerImuneMolecule),
        ('undiff_rtpcr_marker', 'undiff_rtpcr_marker_passage_number', UndifferentiatedMorphologyMarkerRtPcr, UndifferentiatedMorphologyMarkerRtPcrMolecule),
        ('undiff_facs_marker', 'undiff_facs_marker_passage_number', UndifferentiatedMorphologyMarkerFacs, UndifferentiatedMorphologyMarkerFacsMolecule),
    )

    for (hescreg_slug, hescreg_slug_passage_number, marker_model, marker_molecule_model) in undiff_types:
        aux_imune_rtpcr_facs(hescreg_slug, hescreg_slug_passage_number, marker_model, marker_molecule_model)

    # UndifferentiatedMorphologyMarkerMorphology

    if any([valuef(x) for x in (
        'undiff_morphology_markers_passage_number',
        'undiff_morphology_markers_description',
        'undiff_morphology_markers_enc_filename'
    )]):

        UndifferentiatedMorphologyMarkerMorphology(
            cell_line=cell_line,
            passage_number=valuef('undiff_morphology_markers_passage_number'),
            description=valuef('undiff_morphology_markers_description'),
            data_url=aux_hescreg_data_url(valuef('undiff_morphology_markers_enc_filename')),
        ).save()

    # UndifferentiatedMorphologyMarkerExpressionProfile

    if any([valuef(x) for x in (
        'undiff_exprof_markers_method_name',
        'undiff_exprof_markers_weblink',
        'undiff_exprof_markers_enc_filename',
        'undiff_exprof_markers_passage_number',
    )]):

        marker = UndifferentiatedMorphologyMarkerExpressionProfile(
            cell_line=cell_line,
            method=valuef('undiff_exprof_markers_method_name'),
            passage_number=valuef('undiff_exprof_markers_passage_number'),
            data_url=valuef('undiff_exprof_markers_weblink'),
            uploaded_data_url=aux_hescreg_data_url(valuef('undiff_exprof_markers_enc_filename')),
        )

        marker.save()

        if valuef('undiff_exprof_expression_array_marker'):
            aux_molecule_result(marker, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_expression_array_marker'))
        elif valuef('undiff_exprof_rna_sequencing_marker'):
            aux_molecule_result(marker, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_rna_sequencing_marker'))
        elif valuef('undiff_exprof_proteomics_marker'):
            aux_molecule_result(marker, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_proteomics_marker'))


# -----------------------------------------------------------------------------
# Format integrity error

def format_integrity_error(e):
    return re.split(r'\n', e.message)[0]

# -----------------------------------------------------------------------------
