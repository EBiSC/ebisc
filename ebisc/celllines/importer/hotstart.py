import os
import re
import json
import functools

import logging
logger = logging.getLogger('management.commands')

from ..models import *


'''
This is HotsStart JSON data importer.
'''


# -----------------------------------------------------------------------------
# Convert JSON values to python values

def value_of_json(source, field, cast=None):

    if cast == 'bool':

        if source.get(field, None) == '1':
            return True
        else:
            return False

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
        return source.get(field, None)


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
        disease, created = Disease.objects.get_or_create(
            icdcode=valuef('disease_doid'),
            disease=valuef('disease_doid_name'),
        )

        if created:
            logger.info('Found new disease: %s' % disease)

        synonyms = ', '.join([s.split('EXACT')[0].strip() for s in valuef('disease_doid_synonyms').split(',')])

        if synonyms != '':
            disease.synonyms = synonyms
            disease.save()

    return disease


@inject_valuef
def parse_cell_type(valuef, source):

    cell_type, created = Celltype.objects.get_or_create(
        celltype=valuef('primary_celltype_ont_name'),
    )

    if created:
        logger.info('Found new cell type: %s' % cell_type)

    return cell_type


@inject_valuef
def parse_organization(valuef, source):

    # Organization

    organization, created = Organization.objects.get_or_create(
        organizationname=valuef('name')
    )
    if created:
        logger.info('Found new organization: %s' % organization)

    if valuef('role') == 'Generator':

        return (organization, 'generator')

    elif valuef('role') == 'Generator':

        return (organization, 'owner')

    else:

        # Other organization roles

        organization_role, created = Celllineorgtype.objects.get_or_create(
            celllineorgtype=valuef('role')
        )
        if created:
            logger.info('Found new organization type: %s' % organization_role)

        # Cell line organization

        return (organization, organization_role)


@inject_valuef
def parse_donor(valuef, source):

    gender = valuef('gender_primary_cell', 'gender')

    try:
        donor = Donor.objects.get(biosamplesid=valuef('biosamples_donor_id'))

        if donor.gender != gender:
            logger.warn('Changing donor gender from %s to %s' % (donor.gender, gender))
            donor.gender = gender

    except Donor.DoesNotExist:
        donor = Donor(
            biosamplesid=valuef('biosamples_donor_id'),
            providerdonorid=', '.join(valuef('internal_donor_id')) if valuef('internal_donor_id') is not None else '',
            gender=gender,
        )

    donor.save()

    return donor


@inject_valuef
def parse_legal(valuef, source, cell_line):

    if valuef('informed_consent_flag', 'bool'):

        cell_line_legal = CellLineLegal(
            cell_line=cell_line,
            donor_consent=valuef('informed_consent_flag', 'bool'),
        )

        cell_line_legal.save()


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

    cell_line_vector = CellLineIntegratingVector(
        cell_line=cell_line,
        vector=vector,
        virus=term_list_value_of_json(source, 'integrating_vector_virus_type', Virus),
        transposon=term_list_value_of_json(source, 'integrating_vector_transposon_type', Transposon),
        excisable=valuef('excisable_vector_flag', 'bool'),
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

    cell_line_vector = CellLineNonIntegratingVector(
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

    cell_line_derivation = Celllinederivation(
        cell_line=cell_line,
        primarycelldevelopmentalstage=term_list_value_of_json(source, 'dev_stage_primary_cell', PrimaryCellDevelopmentalStage),
        primarycelltypename=valuef('primary_celltype_ont_name'),
        selectioncriteriaforclones=valuef('selection_of_clones'),
        xenofreeconditions=valuef('derivation_xeno_graft_free_flag', 'bool'),
        derivedundergmp=valuef('derivation_gmp_ips_flag', 'bool'),
    )

    logger.info('Added cell line derivation: %s' % cell_line_derivation)

    cell_line_derivation.save()


@inject_valuef
def parse_culture_condions(valuef, source, cell_line):

    cell_line_culture_conditions = Celllinecultureconditions(
        cell_line=cell_line,

        surfacecoating=term_list_value_of_json(source, 'surface_coating', SurfaceCoating),

        feedercellid=valuef('feeder_cells_ont_id'),
        feedercelltype=valuef('feeder_cells_name'),

        passagemethod=term_list_value_of_json(source, 'passage_method', PassageMethod),
        enzymatically=term_list_value_of_json(source, 'passage_method_enzymatically', Enzymatically),
        enzymefree=term_list_value_of_json(source, 'passage_method_enzyme_free', EnzymeFree),

        o2concentration=valuef('o2_concentration', 'int'),
        co2concentration=valuef('co2_concentration', 'int'),
    )

    cell_line_culture_conditions.save()

    # Culture medium

    def parse_supplements(cell_line_culture_conditions, supplements):

        if supplements is None:
            return

        else:
            for supplement in supplements:
                (supplement, amount, unit) = supplement.split('###')
                CellLineCultureMediumSupplement(
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
        CellLinePublication(
            cell_line=cell_line,
            reference_type='pubmed',
            reference_id=valuef('registration_reference_publication_pubmed_id', 'int'),
            reference_url=CellLinePublication.pubmed_url_from_id(valuef('registration_reference_publication_pubmed_id', 'int')),
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
        CellLineCharacterization(
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
#  Importer

def import_data(basedir):

    for f in os.listdir(basedir):

        logger.info('Importing %s' % f)

        with open(os.path.join(basedir, f), 'r') as fi:

            source = json.load(fi)
            valuef = functools.partial(value_of_json, source)

            logger.info('Importing cell line %s' % valuef('name'))

            cell_line = Cellline(
                biosamplesid=valuef('biosamples_id'),
                hescregid=valuef('id'),
                celllinename=valuef('name'),
                celllineprimarydisease=parse_disease(source),
                celllinecelltype=parse_cell_type(source),
                celllinenamesynonyms=', '.join(valuef('alternate_name')) if valuef('alternate_name') is not None else '',
                donor=parse_donor(source),
                donor_age=valuef('donor_age', 'age_range'),
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

            cell_line.save()

            for organization, organization_role in organizations:

                cell_line_organization, created = Celllineorganization.objects.get_or_create(
                    orgcellline=cell_line,
                    organization=organization,
                    celllineorgtype=organization_role,
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
            parse_culture_condions(source, cell_line)
            parse_karyotyping(source, cell_line)
            parse_publications(source, cell_line)
            parse_characterization(source, cell_line)
            parse_characterization_markers(source, cell_line)

            # Final save
            cell_line.save()

# -----------------------------------------------------------------------------
