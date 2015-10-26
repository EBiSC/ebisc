import re
import functools

import logging
logger = logging.getLogger('management.commands')

from django.db import IntegrityError

from .utils import format_integrity_error


from ebisc.celllines.models import  \
    AgeRange,  \
    CellType,  \
    Country,  \
    Gender,  \
    Molecule,  \
    MoleculeReference,  \
    Virus,  \
    Transposon,  \
    Unit,  \
    Donor,  \
    Disease,  \
    CelllineCultureConditions,  \
    CultureMediumOther,  \
    CelllineCultureMediumSupplement,  \
    CelllineDerivation,  \
    NonIntegratingVector,  \
    IntegratingVector,  \
    CelllineNonIntegratingVector,  \
    CelllineIntegratingVector,  \
    CelllineCharacterization,  \
    UndifferentiatedMorphologyMarkerImune,  \
    UndifferentiatedMorphologyMarkerImuneMolecule,  \
    UndifferentiatedMorphologyMarkerRtPcr,  \
    UndifferentiatedMorphologyMarkerRtPcrMolecule,  \
    UndifferentiatedMorphologyMarkerFacs,  \
    UndifferentiatedMorphologyMarkerFacsMolecule,  \
    UndifferentiatedMorphologyMarkerMorphology,  \
    UndifferentiatedMorphologyMarkerExpressionProfile,  \
    UndifferentiatedMorphologyMarkerExpressionProfileMolecule,  \
    CelllineEthics,  \
    Organization,  \
    CelllineOrgType,  \
    CelllinePublication,  \
    CelllineKaryotype,  \
    CelllineDiseaseGenotype, \
    CelllineGenotypingSNP, \
    CelllineGenotypingRsNumber, \
    CelllineHlaTyping, \
    CelllineStrFingerprinting, \
    CelllineGenomeAnalysis, \
    CelllineGeneticModification, \
    GeneticModificationTransgeneExpression, \
    GeneticModificationGeneKnockOut, \
    GeneticModificationGeneKnockIn, \
    GeneticModificationIsogenic


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

    if valuef('disease_flag') == 0:
        return None

    else:
        if valuef('disease_doid_synonyms') is None:
            synonyms = None
        else:
            synonyms = ', '.join([s.split('EXACT')[0].strip() for s in valuef('disease_doid_synonyms').split(',')])

        try:
            disease, created = Disease.objects.update_or_create(
                icdcode=valuef('disease_doid'),
                disease=valuef('disease_doid_name'),
                defaults={'synonyms': synonyms}
            )
        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            return None

        if created:
            logger.info('Found new disease: %s' % disease)

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

    organization, created = Organization.objects.get_or_create(name=valuef('name'))

    if created:
        logger.info('Found new organization: %s' % organization)

    if valuef('role') == 'Generator':
        return (organization, 'generator')

    elif valuef('role') == 'Owner':
        return (organization, 'owner')

    else:
        # Other organization roles
        organization_role, created = CelllineOrgType.objects.get_or_create(cell_line_org_type=valuef('role'))

        if created:
            logger.info('Found new organization type: %s' % organization_role)

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
            karyotype=valuef('donor_karyotype'),
        )

    try:
        donor.save()
    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

    return donor


@inject_valuef
def parse_ethics(valuef, source, cell_line):

    cell_line_ethics, created = CelllineEthics.objects.get_or_create(cell_line=cell_line)

    cell_line_ethics.donor_consent = valuef('hips_consent_obtained_from_donor_of_tissue_flag', 'nullbool')
    cell_line_ethics.no_pressure_statement = valuef('hips_no_pressure_stat_flag', 'nullbool')
    cell_line_ethics.no_inducement_statement = valuef('hips_no_inducement_stat_flag', 'nullbool')
    cell_line_ethics.donor_consent_form = valuef('hips_informed_consent_flag', 'nullbool')
    cell_line_ethics.known_location_of_consent_form = valuef('hips_holding_original_donor_consent_flag', 'nullbool')
    cell_line_ethics.copy_of_consent_form_obtainable = valuef('hips_holding_original_donor_consent_copy_of_existing_flag', 'nullbool')
    cell_line_ethics.obtain_new_consent_form = valuef('hips_arrange_obtain_new_consent_form_flag', 'nullbool')
    cell_line_ethics.donor_recontact_agreement = valuef('hips_donor_recontact_agreement_flag', 'nullbool')
    cell_line_ethics.consent_anticipates_donor_notification_research_results = valuef('hips_consent_anticipates_donor_notification_research_results_flag', 'nullbool')
    cell_line_ethics.donor_expects_notification_health_implications = valuef('hips_donor_expects_notification_health_implications_flag', 'nullbool')
    cell_line_ethics.copy_of_donor_consent_information_english_obtainable = valuef('hips_provide_copy_of_donor_consent_information_english_flag', 'nullbool')
    cell_line_ethics.copy_of_donor_consent_form_english_obtainable = valuef('hips_provide_copy_of_donor_consent_english_flag', 'nullbool')

    cell_line_ethics.consent_permits_ips_derivation = valuef('hips_consent_permits_ips_derivation_flag', 'nullbool')
    cell_line_ethics.consent_pertains_specific_research_project = valuef('hips_consent_pertains_specific_research_project_flag', 'nullbool')
    cell_line_ethics.consent_permits_future_research = valuef('hips_consent_permits_future_research_flag', 'nullbool')
    cell_line_ethics.future_research_permitted_specified_areas = valuef('hips_future_research_permitted_specified_areas_flag', 'nullbool')
    cell_line_ethics.future_research_permitted_areas = valuef('hips_future_research_permitted_areas')
    cell_line_ethics.consent_permits_clinical_treatment = valuef('hips_consent_permits_clinical_treatment_flag', 'nullbool')
    cell_line_ethics.formal_permission_for_distribution = valuef('hips_formal_permission_for_distribution_flag', 'nullbool')
    cell_line_ethics.consent_permits_research_by_academic_institution = valuef('hips_consent_permits_research_by_academic_institution_flag', 'nullbool')
    cell_line_ethics.consent_permits_research_by_org = valuef('hips_consent_permits_research_by_org_flag', 'nullbool')
    cell_line_ethics.consent_permits_research_by_non_profit_company = valuef('hips_consent_permits_research_by_non_profit_company_flag', 'nullbool')
    cell_line_ethics.consent_permits_research_by_for_profit_company = valuef('hips_consent_permits_research_by_for_profit_company_flag', 'nullbool')
    cell_line_ethics.consent_permits_development_of_commercial_products = valuef('hips_consent_permits_development_of_commercial_products_flag', 'nullbool')
    cell_line_ethics.consent_expressly_prevents_commercial_development = valuef('hips_consent_expressly_prevents_commercial_development_flag', 'nullbool')
    cell_line_ethics.consent_expressly_prevents_financial_gain = valuef('hips_consent_expressly_prevents_financial_gain_flag', 'nullbool')
    cell_line_ethics.further_constraints_on_use = valuef('hips_further_constraints_on_use_flag', 'nullbool')
    cell_line_ethics.further_constraints_on_use_desc = valuef('hips_further_constraints_on_use')

    cell_line_ethics.consent_expressly_permits_indefinite_storage = valuef('hips_consent_expressly_permits_indefinite_storage_flag', 'nullbool')
    cell_line_ethics.consent_prevents_availiability_to_worldwide_research = valuef('hips_consent_prevents_availiability_to_worldwide_research_flag', 'nullbool')

    cell_line_ethics.consent_permits_genetic_testing = valuef('hips_consent_permits_genetic_testing_flag', 'nullbool')
    cell_line_ethics.consent_permits_testing_microbiological_agents_pathogens = valuef('hips_consent_permits_testing_microbiological_agents_pathogens_flag', 'nullbool')
    cell_line_ethics.derived_information_influence_personal_future_treatment = valuef('hips_derived_information_influence_personal_future_treatment_flag', 'nullbool')

    cell_line_ethics.donor_data_protection_informed = valuef('hips_donor_data_protection_informed_flag', 'nullbool')
    cell_line_ethics.donated_material_code = valuef('hips_donated_material_code_flag', 'nullbool')
    cell_line_ethics.donated_material_rendered_unidentifiable = valuef('hips_donated_material_rendered_unidentifiable_flag', 'nullbool')
    cell_line_ethics.genetic_information_exists = valuef('genetic_information_associated_flag', 'nullbool')
    cell_line_ethics.genetic_information_access_policy = valuef('hips_genetic_information_access_policy')
    cell_line_ethics.genetic_information_available = valuef('genetic_information_available_flag', 'nullbool')

    cell_line_ethics.consent_permits_access_medical_records = valuef('hips_consent_permits_access_medical_records_flag', 'nullbool')
    cell_line_ethics.consent_permits_access_other_clinical_source = valuef('hips_consent_permits_access_other_clinical_source_flag', 'nullbool')
    cell_line_ethics.medical_records_access_consented = valuef('hips_medical_records_access_consented_flag', 'nullbool')
    cell_line_ethics.medical_records_access_consented_organisation_name = valuef('hips_medical_records_access_consented_organisation_name')

    cell_line_ethics.consent_permits_stop_of_derived_material_use = valuef('hips_consent_permits_stop_of_derived_material_use_flag', 'nullbool')
    cell_line_ethics.consent_permits_stop_of_delivery_of_information_and_data = valuef('hips_consent_permits_delivery_of_information_and_data_flag', 'nullbool')

    cell_line_ethics.authority_approval = valuef('hips_approval_flag', 'nullbool')
    cell_line_ethics.approval_authority_name = valuef('hips_approval_auth_name')
    cell_line_ethics.approval_number = valuef('hips_approval_number')
    cell_line_ethics.ethics_review_panel_opinion_relation_consent_form = valuef('hips_ethics_review_panel_opinion_relation_consent_form_flag', 'nullbool')
    cell_line_ethics.ethics_review_panel_opinion_project_proposed_use = valuef('hips_ethics_review_panel_opinion_project_proposed_use_flag', 'nullbool')

    cell_line_ethics.recombined_dna_vectors_supplier = valuef('hips_recombined_dna_vectors_supplier')
    cell_line_ethics.use_or_distribution_constraints = valuef('hips_use_or_distribution_constraints_flag', 'nullbool')
    cell_line_ethics.use_or_distribution_constraints_desc = valuef('hips_use_or_distribution_constraints')
    cell_line_ethics.third_party_obligations = valuef('hips_third_party_obligations_flag', 'nullbool')
    cell_line_ethics.third_party_obligations_desc = valuef('hips_third_party_obligations')

    if created or cell_line_ethics.is_dirty():
        cell_line_ethics.save()
        return True

    return False


@inject_valuef
def parse_integrating_vector(valuef, source, cell_line):

    if valuef('integrating_vector') == 'other':
        if valuef('integrating_vector_other') is not None:
            vector_name = valuef('integrating_vector_other')
        else:
            vector_name = u'Other'
    else:
        vector_name = valuef('integrating_vector')

    vector, vector_created = IntegratingVector.objects.get_or_create(name=vector_name)

    if vector_created:
        logger.info('Added integrating vector: %s' % vector)

    cell_line_integrating_vector, cell_line_integrating_vector_created = CelllineIntegratingVector.objects.get_or_create(cell_line=cell_line)

    cell_line_integrating_vector.vector = vector
    cell_line_integrating_vector.virus = term_list_value_of_json(source, 'integrating_vector_virus_type', Virus)
    cell_line_integrating_vector.transposon = term_list_value_of_json(source, 'integrating_vector_transposon_type', Transposon)
    cell_line_integrating_vector.excisable = valuef('excisable_vector_flag', 'bool')
    cell_line_integrating_vector.absence_reprogramming_vectors = valuef('reprogramming_vectors_absence_flag', 'bool')

    dirty = [cell_line_integrating_vector.is_dirty(check_relationship=True)]

    for gene in [parse_molecule(g) for g in source.get('integrating_vector_gene_list', [])]:
        cell_line_integrating_vector.genes.add(gene)

    if True in dirty:
        if cell_line_integrating_vector_created:
            logger.info('Added integrating vector: %s to cell line %s' % (vector, cell_line))
        else:
            logger.info('Updated integrating vector: %s to cell line %s' % (vector, cell_line))

        cell_line_integrating_vector.save()

        return True

    return False


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

    vector, vector_created = NonIntegratingVector.objects.get_or_create(name=vector_name)

    if vector_created:
        logger.info('Added non-integrating vector: %s' % vector)

    cell_line_non_integrating_vector, cell_line_non_integrating_vector_created = CelllineNonIntegratingVector.objects.get_or_create(cell_line=cell_line)

    cell_line_non_integrating_vector.vector = vector

    dirty = [cell_line_non_integrating_vector.is_dirty(check_relationship=True)]

    for gene in [parse_molecule(g) for g in source.get('non_integrating_vector_gene_list', [])]:
        cell_line_non_integrating_vector.genes.add(gene)

    if True in dirty:
        if cell_line_non_integrating_vector_created:
            logger.info('Added non-integrationg vector %s to cell line %s' % (vector, cell_line))
        else:
            logger.info('Updated non-integrationg vector %s to cell line %s' % (vector, cell_line))

        cell_line_non_integrating_vector.save()

        return True

    return False


@inject_valuef
def parse_derivation(valuef, source, cell_line):

    cell_line_derivation, cell_line_derivation_created = CelllineDerivation.objects.get_or_create(cell_line=cell_line)

    cell_line_derivation.primary_cell_type = parse_cell_type(source)
    cell_line_derivation.primary_cell_developmental_stage = valuef('dev_stage_primary_cell') if valuef('dev_stage_primary_cell') and valuef('dev_stage_primary_cell') != '0' else ''
    cell_line_derivation.tissue_procurement_location = valuef('location_primary_tissue_procurement')
    cell_line_derivation.tissue_collection_date = valuef('collection_date')
    cell_line_derivation.reprogramming_passage_number = valuef('passage_number_reprogrammed')

    cell_line_derivation.selection_criteria_for_clones = valuef('selection_of_clones')
    cell_line_derivation.xeno_free_conditions = valuef('derivation_xeno_graft_free_flag', 'bool')
    cell_line_derivation.derived_under_gmp = valuef('derivation_gmp_ips_flag', 'bool')
    cell_line_derivation.available_as_clinical_grade = valuef('available_clinical_grade_ips_flag', 'bool')

    if cell_line_derivation_created or cell_line_derivation.is_dirty(check_relationship=True):
        try:
            cell_line_derivation.save()

            if cell_line_derivation_created:
                logger.info('Added cell line derivation: %s' % cell_line_derivation)
            else:
                logger.info('Updated cell line derivation: %s' % cell_line_derivation)

            return True

        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            return None

    return False


@inject_valuef
def parse_culture_conditions(valuef, source, cell_line):

    cell_line_culture_conditions, cell_line_culture_conditions_created = CelllineCultureConditions.objects.get_or_create(cell_line=cell_line)

    cell_line_culture_conditions.surface_coating = valuef('surface_coating')
    cell_line_culture_conditions.feeder_cell_id = valuef('feeder_cells_ont_id')
    cell_line_culture_conditions.feeder_cell_type = valuef('feeder_cells_name')
    cell_line_culture_conditions.passage_method = valuef('passage_method')
    cell_line_culture_conditions.enzymatically = valuef('passage_method_enzymatically')
    cell_line_culture_conditions.enzyme_free = valuef('passage_method_enzyme_free')
    cell_line_culture_conditions.o2_concentration = valuef('o2_concentration', 'int')
    cell_line_culture_conditions.co2_concentration = valuef('co2_concentration', 'int')
    cell_line_culture_conditions.passage_number_banked = valuef('passage_number_banked')
    cell_line_culture_conditions.number_of_vials_banked = valuef('number_of_vials_banked')

    if not valuef('culture_conditions_medium_culture_medium') == 'other_medium':
        cell_line_culture_conditions.culture_medium = valuef('culture_conditions_medium_culture_medium')

    dirty = [cell_line_culture_conditions.is_dirty(check_relationship=True)]

    def parse_supplements(cell_line_culture_conditions, supplements):

        old_supplements = set([supplement.supplement for supplement in cell_line_culture_conditions.medium_supplements.all()])

        dirty_supplements = []

        if supplements is None:

            if not old_supplements:
                return []

            else:
                for supplement_name in old_supplements:
                    s = CelllineCultureMediumSupplement.objects.get(cell_line_culture_conditions=cell_line_culture_conditions, supplement=supplement_name)
                    s.delete()
                    dirty_supplements += [True]

        else:
            new_supplements_list = []

            for supplement in supplements:
                (supplement_name, amount, unit) = supplement.split('###')

                new_supplements_list.append((supplement_name))

            new_supplements = set(new_supplements_list)

            # Delete old supplements that are not in new supplements
            for supplement_name in (old_supplements - new_supplements):
                s = CelllineCultureMediumSupplement.objects.get(cell_line_culture_conditions=cell_line_culture_conditions, supplement=supplement_name)
                s.delete()
                dirty_supplements += [True]

            for supplement in supplements:
                (supplement_name, amount, unit) = supplement.split('###')

                # Add new supplements
                if supplement_name in (new_supplements - old_supplements):
                    CelllineCultureMediumSupplement(
                        cell_line_culture_conditions=cell_line_culture_conditions,
                        supplement=supplement_name,
                        amount=amount,
                        unit=term_list_value(unit, Unit),
                    ).save()
                    dirty_supplements += [True]

                # Modify existing if data has changed
                else:
                    cell_line_culture_medium_supplement = CelllineCultureMediumSupplement.objects.get(cell_line_culture_conditions=cell_line_culture_conditions, supplement=supplement_name,)
                    cell_line_culture_medium_supplement.amount = amount
                    cell_line_culture_medium_supplement.unit = term_list_value(unit, Unit)

                    if cell_line_culture_medium_supplement.is_dirty():
                        cell_line_culture_medium_supplement.save()
                        dirty_supplements += [True]

            return dirty_supplements

    if not valuef('culture_conditions_medium_culture_medium') == 'other_medium':

        # Culture medium supplements
        dirty += parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_supplements'))

    else:
        cell_line_culture_medium_other, created = CultureMediumOther.objects.get_or_create(cell_line_culture_conditions=cell_line_culture_conditions)

        cell_line_culture_medium_other.base = valuef('culture_conditions_medium_culture_medium_other_base')
        cell_line_culture_medium_other.protein_source = valuef('culture_conditions_medium_culture_medium_other_protein_source')
        cell_line_culture_medium_other.serum_concentration = valuef('culture_conditions_medium_culture_medium_other_concentration', 'int')

        if created or cell_line_culture_medium_other.is_dirty():
            cell_line_culture_medium_other.save()
            dirty += [True]

        # Culture medium supplements
        dirty += parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_other_supplements'))

    if True in dirty:
        if cell_line_culture_conditions_created:
            logger.info('Added cell line culture conditions: %s' % cell_line_culture_conditions)
        else:
            logger.info('Updated cell line culture conditions: %s' % cell_line_culture_conditions)

        cell_line_culture_conditions.save()

        return True

    return False


@inject_valuef
def parse_karyotyping(valuef, source, cell_line):

    if valuef('karyotyping_flag', 'bool'):

        if valuef('karyotyping_method') == 'other':
            if valuef('karyotyping_method_other'):
                karyotype_method = valuef('karyotyping_method_other')
            else:
                karyotype_method = u'Other'
        else:
            karyotype_method = valuef('karyotyping_method')

        if valuef('karyotyping_karyotype') or valuef('karyotyping_method') or valuef('karyotyping_number_passages'):

            cell_line_karyotype, cell_line_karyotype_created = CelllineKaryotype.objects.get_or_create(cell_line=cell_line)

            cell_line_karyotype.karyotype = valuef('karyotyping_karyotype')
            cell_line_karyotype.karyotype_method = karyotype_method
            cell_line_karyotype.passage_number = valuef('karyotyping_number_passages')

            if cell_line_karyotype_created or cell_line_karyotype.is_dirty(check_relationship=True):
                if cell_line_karyotype_created:
                    logger.info('Added cell line karyotype: %s' % cell_line_karyotype)
                else:
                    logger.info('Updated cell line karyotype: %s' % cell_line_karyotype)

                    cell_line_karyotype.save()

                    return True

            return False


@inject_valuef
def parse_hla_typing(valuef, source, cell_line):

    if valuef('hla_flag', 'bool'):

        if valuef('hla_i_a_all1') or valuef('hla_i_a_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='I',
                hla='A',
                hla_allele_1=valuef('hla_i_a_all1'),
                hla_allele_2=valuef('hla_i_a_all2'),
            ).save

        if valuef('hla_i_b_all1') or valuef('hla_i_b_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='I',
                hla='B',
                hla_allele_1=valuef('hla_i_b_all1'),
                hla_allele_2=valuef('hla_i_b_all2'),
            ).save

        if valuef('hla_i_c_all1') or valuef('hla_i_c_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='I',
                hla='C',
                hla_allele_1=valuef('hla_i_c_all1'),
                hla_allele_2=valuef('hla_i_c_all2'),
            ).save

        if valuef('hla_ii_dp_all1') or valuef('hla_ii_dp_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='II',
                hla='DP',
                hla_allele_1=valuef('hla_ii_dp_all1'),
                hla_allele_2=valuef('hla_ii_dp_all2'),
            ).save

        if valuef('hla_ii_dm_all1') or valuef('hla_ii_dm_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='II',
                hla='DM',
                hla_allele_1=valuef('hla_ii_dm_all1'),
                hla_allele_2=valuef('hla_ii_dm_all2'),
            ).save

        if valuef('hla_ii_doa_all1') or valuef('hla_ii_doa_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='II',
                hla='DOA',
                hla_allele_1=valuef('hla_ii_doa_all1'),
                hla_allele_2=valuef('hla_ii_doa_all2'),
            ).save

        if valuef('hla_ii_dq_all1') or valuef('hla_ii_dq_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='II',
                hla='DQ',
                hla_allele_1=valuef('hla_ii_dq_all1'),
                hla_allele_2=valuef('hla_ii_dq_all2'),
            ).save

        if valuef('hla_ii_dr_all1') or valuef('hla_ii_dr_all2'):
            CelllineHlaTyping(
                cell_line=cell_line,
                hla_class='II',
                hla='DR',
                hla_allele_1=valuef('hla_ii_dr_all1'),
                hla_allele_2=valuef('hla_ii_dr_all2'),
            ).save


@inject_valuef
def parse_str_fingerprinting(valuef, source, cell_line):

    if valuef('fingerprinting_flag', 'bool'):

        if valuef('fingerprinting') is None:
            return

        else:
            for locus in valuef('fingerprinting'):
                (locus, allele1, allele2) = locus.split('###')
                CelllineStrFingerprinting(
                    cell_line=cell_line,
                    locus=locus,
                    allele1=allele1,
                    allele2=allele2,
                ).save()

        logger.info('Added cell STR/Fingerprinting')


@inject_valuef
def parse_genome_analysis(valuef, source, cell_line):

    if valuef('genome_wide_genotyping_flag', 'bool'):

        data_type = None

        if valuef('genome_wide_genotyping_ega'):
            if valuef('genome_wide_genotyping_ega') == 'other':
                if valuef('genome_wide_genotyping_ega_other') is not None:
                    data_type = valuef('genome_wide_genotyping_ega_other')
                else:
                    data_type = u'Other'
            else:
                data_type = valuef('genome_wide_genotyping_ega')

        if data_type or valuef('genome_wide_genotyping_ega_url'):
            cell_line_genome_analysis = CelllineGenomeAnalysis(
                cell_line=cell_line,
                data=data_type,
                link=valuef('genome_wide_genotyping_ega_url'),
            )

            cell_line_genome_analysis.save()

            logger.info('Added cell line genome analysis')


@inject_valuef
def parse_genetic_modifications(valuef, source, cell_line):

    if valuef('genetic_modification_flag', 'bool'):

        def parse_delivery_method(source, source_field, source_field_other):

            if source_field not in source and source_field_other not in source:
                return None

            delivery_method = None

            if valuef(source_field) == 'other':
                if valuef(source_field_other) is not None:
                    delivery_method = valuef(source_field_other)
                else:
                    delivery_method = u'Other'
            else:
                delivery_method = valuef(source_field)

            return delivery_method

        for modification_type in valuef('genetic_modification_types'):
            if modification_type == 'gen_mod_transgene_expression':

                transgene_expression = GeneticModificationTransgeneExpression(
                    cell_line=cell_line,
                    delivery_method=parse_delivery_method(source, 'transgene_delivery_method', 'transgene_delivery_method_other'),
                    virus=term_list_value_of_json(source, 'transgene_viral_method_spec', Virus),
                    transposon=term_list_value_of_json(source, 'transgene_transposon_method_spec', Transposon),
                )

                transgene_expression.save()

                for gene in [parse_molecule(g) for g in source.get('genetic_modification_transgene_expression_list', [])]:
                    logger.info('Added gene: %s' % gene)
                    transgene_expression.genes.add(gene)

                transgene_expression.save()

                logger.info('Added transgene modification: %s' % transgene_expression)

            elif modification_type == 'gen_mod_gene_knock_out':

                gene_knock_out = GeneticModificationGeneKnockOut(
                    cell_line=cell_line,
                    delivery_method=parse_delivery_method(source, 'knockout_delivery_method', 'knockout_delivery_method_other'),
                    virus=term_list_value_of_json(source, 'knockout_viral_method_spec', Virus),
                    transposon=term_list_value_of_json(source, 'knockout_transposon_method_spec', Transposon),
                )

                gene_knock_out.save()

                for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockout_list', [])]:
                    logger.info('Added gene: %s' % gene)
                    gene_knock_out.target_genes.add(gene)

                gene_knock_out.save()

                logger.info('Added gene knock-out modification: %s' % gene_knock_out)

            elif modification_type == 'gen_mod_gene_knock_in':

                gene_knock_in = GeneticModificationGeneKnockIn(
                    cell_line=cell_line,
                    delivery_method=parse_delivery_method(source, 'knockin_delivery_method', 'knockin_delivery_method_other'),
                    virus=term_list_value_of_json(source, 'knockin_viral_method_spec', Virus),
                    transposon=term_list_value_of_json(source, 'knockin_transposon_method_spec', Transposon),
                )

                gene_knock_in.save()

                for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockin_target_gene_list', [])]:
                    logger.info('Added gene: %s' % gene)
                    gene_knock_in.target_genes.add(gene)

                gene_knock_in.save()

                for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockin_transgene_list', [])]:
                    logger.info('Added gene: %s' % gene)
                    gene_knock_in.transgenes.add(gene)

                gene_knock_in.save()

                logger.info('Added gene knock-in modification: %s' % gene_knock_in)

            elif modification_type == 'gen_mod_isogenic_modification':

                isogenic_modification = GeneticModificationIsogenic(
                    cell_line=cell_line,
                    change_type=valuef('genetic_modification_isogenic_modified_locus_change_type'),
                    modified_sequence=valuef('genetic_modification_isogenic_modified_locus'),
                )

                isogenic_modification.save()

                for gene in [parse_molecule(g) for g in source.get('genetic_modification_isogenic_target_locus_list', [])]:
                    logger.info('Added gene: %s' % gene)
                    isogenic_modification.target_locus.add(gene)

                isogenic_modification.save()

                logger.info('Added gene isogenic modification: %s' % isogenic_modification)


@inject_valuef
def parse_disease_associated_genotype(valuef, source, cell_line):

    if valuef('carries_disease_phenotype_associated_variants_flag', 'bool') and valuef('variant_of_interest_flag', 'bool'):

        cell_line_disease_genotype, created = CelllineDiseaseGenotype.objects.get_or_create(cell_line=cell_line)

        cell_line_disease_genotype = CelllineDiseaseGenotype(
            cell_line=cell_line,

            allele_carried=valuef('rs_allele_carried'),
            cell_line_form=valuef('rs_cell_line_variant_homozygote_heterozygote'),

            chormosome=valuef('variant_details_chromosome'),
            coordinate=valuef('variant_details_coordinate'),
            reference_allele=valuef('variant_details_ref_allele'),
            alternative_allele=valuef('variant_details_alt_allele'),
            protein_sequence_variants=valuef('description_sequence_changes'),
        )

        if valuef('variant_details_assembly'):
            cell_line_disease_genotype.assembly = valuef('variant_details_assembly')
        elif valuef('variant_details_assembly_other'):
            cell_line_disease_genotype.assembly = valuef('variant_details_assembly_other')

        cell_line_disease_genotype.save()

        def parse_snps(cell_line_disease_genotype, snps):

            if snps is None:
                return

            else:
                for snp in snps:
                    (gene_name, chromosomal_position) = snp.split('###')
                    CelllineGenotypingSNP(
                        disease_genotype=cell_line_disease_genotype,
                        gene_name=gene_name,
                        chromosomal_position=chromosomal_position,
                    ).save()

        def parse_rs_numbers(cell_line_disease_genotype, rs_numbers):

            if rs_numbers is None:
                return

            else:
                for rs_number in rs_numbers:
                    (rs_number, link) = rs_number.split('###')
                    CelllineGenotypingRsNumber(
                        disease_genotype=cell_line_disease_genotype,
                        rs_number=rs_number,
                        link=link,
                    ).save()

        parse_snps(cell_line_disease_genotype, valuef('snp_list'))
        parse_rs_numbers(cell_line_disease_genotype, valuef('rs_number_list'))

        # Final save

        cell_line_disease_genotype.save()
        logger.info('Added cell line disease associated genotype: %s' % cell_line_disease_genotype)


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
