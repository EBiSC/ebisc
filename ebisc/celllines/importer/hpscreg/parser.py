import re
import os
import requests
import functools

import logging
logger = logging.getLogger('management.commands')

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.db import IntegrityError

from .utils import format_integrity_error

from ebisc.celllines.models import  \
    AgeRange,  \
    CellType,  \
    Cellline,  \
    Gender,  \
    Molecule,  \
    MoleculeReference,  \
    Virus,  \
    Transposon,  \
    Unit,  \
    Donor,  \
    DonorDisease,  \
    DonorDiseaseVariant, \
    DonorGenomeAnalysis, \
    DonorGenomeAnalysisFile, \
    Disease,  \
    CelllineDisease,  \
    CelllineCultureConditions,  \
    CultureMediumOther,  \
    CelllineCultureMediumSupplement,  \
    CelllineDerivation,  \
    NonIntegratingVector,  \
    IntegratingVector,  \
    CelllineNonIntegratingVector,  \
    CelllineIntegratingVector,  \
    CelllineVectorFreeReprogrammingFactors,  \
    VectorFreeReprogrammingFactor, \
    CelllineCharacterization,  \
    CelllineCharacterizationMarkerExpression, \
    CelllineCharacterizationMarkerExpressionMethod, \
    CelllineCharacterizationMarkerExpressionMethodFile, \
    CelllineCharacterizationPluritest, \
    CelllineCharacterizationPluritestFile, \
    CelllineCharacterizationEpipluriscore, \
    CelllineCharacterizationEpipluriscoreFile, \
    CelllineCharacterizationUndifferentiatedMorphologyFile, \
    CelllineCharacterizationHpscScorecard, \
    CelllineCharacterizationHpscScorecardReport, \
    CelllineCharacterizationHpscScorecardScorecard, \
    UndifferentiatedMorphologyMarkerImune,  \
    UndifferentiatedMorphologyMarkerImuneMolecule,  \
    UndifferentiatedMorphologyMarkerRtPcr,  \
    UndifferentiatedMorphologyMarkerRtPcrMolecule,  \
    UndifferentiatedMorphologyMarkerFacs,  \
    UndifferentiatedMorphologyMarkerFacsMolecule,  \
    UndifferentiatedMorphologyMarkerMorphology,  \
    UndifferentiatedMorphologyMarkerExpressionProfile,  \
    UndifferentiatedMorphologyMarkerExpressionProfileMolecule,  \
    Organization,  \
    CelllineOrgType,  \
    CelllinePublication,  \
    CelllineKaryotype,  \
    CelllineHlaTyping, \
    CelllineStrFingerprinting, \
    CelllineGenomeAnalysis, \
    CelllineGenomeAnalysisFile, \
    ModificationVariantDisease, \
    ModificationVariantNonDisease, \
    ModificationIsogenicDisease, \
    ModificationIsogenicNonDisease, \
    ModificationTransgeneExpressionDisease, \
    ModificationTransgeneExpressionNonDisease, \
    ModificationGeneKnockOutDisease, \
    ModificationGeneKnockOutNonDisease, \
    ModificationGeneKnockInDisease, \
    ModificationGeneKnockInNonDisease


# -----------------------------------------------------------------------------
# Convert JSON values to python values

def get_in_json(source, path):
    if isinstance(path, str):
        return source[path]
    else:
        # path is a list
        if len(path) == 1:
            return get_in_json(source, path[0])
        else:
            return get_in_json(source[path[0]], path[1:])


def value_of_json(source, path, cast=None):

    if cast == 'bool':
        try:
            if get_in_json(source, path) == '1':
                return True
            else:
                return False
        except KeyError:
            return False

    elif cast == 'nullbool':
        try:
            if get_in_json(source, path) == '1':
                return True
            elif get_in_json(source, path) == '0':
                return False
            else:
                return None
        except KeyError:
            return None

    elif cast == 'extended_bool':
        try:
            if get_in_json(source, path) == '1':
                return 'yes'
            elif get_in_json(source, path) == '0':
                return 'no'
            elif get_in_json(source, path) == 'unknown':
                return 'unknown'
            else:
                return 'unknown'
        except KeyError:
            return None

    elif cast == 'int':
        try:
            return int(get_in_json(source, path))
        except KeyError:
            return None
        except:
            logger.warn('Invalid field value for int: %s=%s' % (path, get_in_json(source, path)))
            return None

    elif cast == 'gender':
        try:
            return Gender.objects.get(name=get_in_json(source, path))
        except KeyError:
            return None
        except Gender.DoesNotExist:
            logger.warn('Invalid donor gender: %s' % get_in_json(source, path))
            return None

    elif cast == 'age_range':
        try:
            value = get_in_json(source, path)
            if value == '---':
                return None
            return AgeRange.objects.get(name=value)
        except KeyError:
            return None
        except AgeRange.DoesNotExist:
            logger.warn('Invalid age range: %s' % get_in_json(source, path))
            return None

    else:
        try:
            value = get_in_json(source, path)
            if isinstance(value, str) or isinstance(value, unicode):
                return value.strip()
            else:
                return value
        except KeyError:
            return None


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


def inject_valuef(func):
    def wrapper(source, *args):
        args = [functools.partial(value_of_json, source), source] + list(args)
        return func(*args)
    return wrapper


# -----------------------------------------------------------------------------
# Parse and save files

def value_of_file(source_file_link, source_file_name, file_field, current_enc=None):

    # Save file for file_field and return its enc_hash

    if source_file_link == '':
        file_field.delete()
        return None

    if source_file_name is None:
        source_filename = os.path.basename(source_file_link)
    else:
        source_filename = source_file_name

    if file_field:
        current_filename = os.path.basename(file_field.name)
    else:
        current_filename = ''

    source_enc = os.path.splitext(os.path.basename(source_file_link))[0]

    if source_enc is not None and current_enc is not None and source_enc == current_enc:
        return current_enc

    logger.info('Fetching data file from %s' % source_file_link)

    response = requests.get(source_file_link, stream=True, auth=(settings.HPSCREG.get('username'), settings.HPSCREG.get('password')))

    with NamedTemporaryFile(delete=True) as f:
        for chunk in response.iter_content(10240):
            f.write(chunk)

        f.seek(0)
        file_field.save(source_filename, File(f), save=False)
        file_field.instance.save()

        f.seek(0)
        return source_enc


# -----------------------------------------------------------------------------
# Specific parsers

# -----------------------------------------------------------------------------
# Cell line diseases

def parse_cell_line_diseases(source, cell_line):

    cell_line_diseases_old = list(cell_line.diseases.all().order_by('id'))
    cell_line_diseases_old_ids = set([d.id for d in cell_line_diseases_old])

    # Parse cell lines diseases (and correctly save them)

    cell_line_diseases_new = []

    for ds in source.get('diseases', []):
        cell_line_diseases_new.append(parse_cell_line_disease(ds, cell_line))

    cell_line_diseases_new_ids = set([d.id for d in cell_line_diseases_new if d is not None])

    # Delete existing cell line diseases that are not present in new data

    to_delete = cell_line_diseases_old_ids - cell_line_diseases_new_ids

    for cell_line_disease in [cd for cd in cell_line_diseases_old if cd.id in to_delete]:
        logger.info('Deleting obsolete cell line disease %s' % cell_line_disease)
        cell_line_disease.delete()

    # Check for changes (dirty)

    if (cell_line_diseases_old_ids != cell_line_diseases_new_ids):
        return True
    else:
        def diseases_equal(a, b):
            return (
                a.primary_disease == b.primary_disease and
                a.notes == b.notes and
                a.disease_not_normalised == b.disease_not_normalised
            )
        for (old, new) in zip(cell_line_diseases_old, cell_line_diseases_new):
            if not diseases_equal(old, new):
                return True

    return False


@inject_valuef
def parse_cell_line_disease(valuef, source, cell_line):

    disease = parse_disease(source)

    genetic_modification_types = (
        ('disease_variants_old', 'disease_variants_old_ids', 'disease_variants_new', 'disease_variants_new_ids', 'Variant'),
        ('disease_isogenic_old', 'disease_isogenic_old_ids', 'disease_isogenic_new', 'disease_isogenic_new_ids', 'Isogenic modification'),
        ('disease_transgene_old', 'disease_transgene_old_ids', 'disease_transgene_new', 'disease_transgene_new_ids', 'Transgene expression'),
        ('disease_knockout_old', 'disease_knockout_old_ids', 'disease_knockout_new', 'disease_knockout_new_ids', 'Gene knock-out'),
        ('disease_knockin_old', 'disease_knockin_old_ids', 'disease_knockin_new', 'disease_knockin_new_ids', 'Gene knock-in'),
    )

    for (list_old, list_old_ids, list_new, list_new_ids, modification_type) in genetic_modification_types:
        list_old = []

    if disease is not None:

        cell_line_disease, created = CelllineDisease.objects.update_or_create(
            cell_line=cell_line,
            disease=disease,
            disease_not_normalised=valuef('other'),
            defaults={
                'primary_disease': valuef('primary', 'bool'),
                'notes': valuef('free_text'),
            }
        )

        for (list_old, list_old_genes, list_new, list_new_genes, modification_type) in genetic_modification_types:

            # Process disease variants. Create new ones, update existing with new data and delete variants that are no longer in hPSCreg data

            if modification_type == 'Variant':
                list_old = list(cell_line_disease.genetic_modification_cellline_disease_variants.all().order_by('id'))
            elif modification_type == 'Isogenic modification':
                list_old = list(cell_line_disease.genetic_modification_cellline_disease_isogenic.all().order_by('id'))
            elif modification_type == 'Transgene expression':
                list_old = list(cell_line_disease.genetic_modification_cellline_disease_transgene_expression.all().order_by('id'))
            elif modification_type == 'Gene knock-out':
                list_old = list(cell_line_disease.genetic_modification_cellline_disease_gene_knock_out .all().order_by('id'))
            elif modification_type == 'Gene knock-in':
                list_old = list(cell_line_disease.genetic_modification_cellline_disease_gene_knock_in.all().order_by('id'))

            list_old_ids = set([v.modification_id for v in list_old])

            list_new = []

            for variant in source.get('variants', []):
                if variant["type"] == modification_type:
                    list_new.append(parse_cell_line_disease_variant(variant, cell_line_disease))

            list_new_ids = set([v.modification_id for v in list_new if v is not None])

            # Delete existing disease variants that are not present in new data

            to_delete = list_old_ids - list_new_ids

            for disease_variant in [vd for vd in list_old if vd.modification_id in to_delete]:
                logger.info('Deleting obsolete disease variant %s' % disease_variant)
                disease_variant.delete()

        if created:
            logger.info('Created new cell line disease: %s' % disease)

        return cell_line_disease

    else:
        return None


@inject_valuef
def parse_cell_line_disease_variant(valuef, source, cell_line_disease):

    if valuef('gene') is not None:
        gene = parse_gene(valuef('gene'))
    else:
        gene = None

    if valuef('transgene') is not None:
        transgene = parse_gene(valuef('transgene'))
    else:
        transgene = None

    virus = None

    if valuef('delivery_method_virus') == 'Other' and valuef('delivery_method_virus_other') is not None:
        virus = term_list_value_of_json(source, 'delivery_method_virus_other', Virus)
    elif valuef('delivery_method_virus') is not None:
        virus = term_list_value_of_json(source, 'delivery_method_virus', Virus)

    transposon = None

    if valuef('delivery_method_transposon_type') == 'Other' and valuef('delivery_method_transposon_type_other') is not None:
        transposon = term_list_value_of_json(source, 'delivery_method_transposon_type_other', Transposon)
    elif valuef('delivery_method_transposon_type') is not None:
        transposon = term_list_value_of_json(source, 'delivery_method_transposon_type', Transposon)

    delivery_method = None

    if valuef('delivery_method') == 'Other' and valuef('delivery_method_other') is not None:
        delivery_method = valuef('delivery_method_other')
    elif valuef('delivery_method') is not None:
        delivery_method = valuef('delivery_method')

    isogenic_modificaton_type = None

    if valuef('isogenic_change_type') == 'Other' and valuef('isogenic_change_type_other') is not None:
        isogenic_modificaton_type = valuef('isogenic_change_type_other')
    elif valuef('isogenic_change_type') is not None:
        isogenic_modificaton_type = valuef('isogenic_change_type')

    if valuef('type') == 'Variant':

        cell_line_disease_variant, created = ModificationVariantDisease.objects.update_or_create(
            cellline_disease=cell_line_disease,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'nucleotide_sequence_hgvs': valuef('nucleotide_sequence_hgvs'),
                'protein_sequence_hgvs': valuef('protein_sequence_hgvs'),
                'zygosity_status': valuef('zygosity_status'),
                'clinvar_id': valuef('clinvar_id'),
                'dbsnp_id': valuef('dbsnp_id'),
                'dbvar_id': valuef('dbvar_id'),
                'publication_pmid': valuef('publication_pmid'),
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new cell line disease variant: %s , gene: %s' % (cell_line_disease_variant, gene))

    elif valuef('type') == 'Isogenic modification':

        cell_line_disease_variant, created = ModificationIsogenicDisease.objects.update_or_create(
            cellline_disease=cell_line_disease,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'nucleotide_sequence_hgvs': valuef('nucleotide_sequence_hgvs'),
                'protein_sequence_hgvs': valuef('protein_sequence_hgvs'),
                'zygosity_status': valuef('zygosity_status'),
                'modification_type': isogenic_modificaton_type,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new cell line disease variant: %s , gene: %s' % (cell_line_disease_variant, gene))

    elif valuef('type') == 'Transgene expression':

        cell_line_disease_variant, created = ModificationTransgeneExpressionDisease.objects.update_or_create(
            cellline_disease=cell_line_disease,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new cell line disease variant: %s , gene: %s' % (cell_line_disease_variant, gene))

    elif valuef('type') == 'Gene knock-out':

        cell_line_disease_variant, created = ModificationGeneKnockOutDisease.objects.update_or_create(
            cellline_disease=cell_line_disease,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new cell line disease variant: %s , gene: %s' % (cell_line_disease_variant, gene))

    elif valuef('type') == 'Gene knock-in':

        cell_line_disease_variant, created = ModificationGeneKnockInDisease.objects.update_or_create(
            cellline_disease=cell_line_disease,
            modification_id=valuef('id'),
            defaults={
                'target_gene': gene,
                'transgene': transgene,
                'chromosome_location': valuef('chromosome_location'),
                'chromosome_location_transgene': valuef('transgene_chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new cell line disease variant: %s , gene: %s' % (cell_line_disease_variant, gene))

    else:

        return None

    return cell_line_disease_variant


# -----------------------------------------------------------------------------
# Donor

@inject_valuef
def parse_donor(valuef, source):

    gender = term_list_value(valuef('gender'), Gender)

    try:
        donor = Donor.objects.get(biosamples_id=valuef('biosamples_id'))

        if donor.gender != gender and gender is not None:
            logger.warn('Changing donor gender from %s to %s' % (donor.gender, gender))
            donor.gender = gender

        if valuef('internal_ids') is not None:
            donor.provider_donor_ids = valuef('internal_ids')
        if valuef('ethnicity') is not None:
            donor.ethnicity = valuef('ethnicity')
        if valuef('family_history') is not None:
            donor.family_history = valuef('family_history')
        if valuef('medical_history') is not None:
            donor.medical_history = valuef('medical_history')
        if valuef('clinical_information') is not None:
            donor.clinical_information = valuef('clinical_information')

        dirty = [donor.is_dirty(check_relationship=True)]

        if True in dirty:
            logger.info('Updated donor: %s' % donor)

            donor.save()

    except Donor.DoesNotExist:
        donor = Donor(
            biosamples_id=valuef('biosamples_id'),
            provider_donor_ids=valuef('internal_ids'),
            gender=gender,
            ethnicity=valuef('ethnicity'),
            family_history=valuef('family_history'),
            medical_history=valuef('medical_history'),
            clinical_information=valuef('clinical_information')
        )

        try:
            donor.save()
        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            return None

    parse_donor_diseases(source, donor)
    parse_donor_genome_analysis(source, donor)

    return donor


# -----------------------------------------------------------------------------
# Donor diseases

def parse_donor_diseases(source, donor):

    # Parse donor diseases (and correctly save them)

    donor_diseases_old = list(donor.diseases.all().order_by('id'))
    donor_diseases_old_ids = set([d.id for d in donor_diseases_old])

    donor_diseases_new = []

    for ds in source.get('diseases', []):
        donor_diseases_new.append(parse_donor_disease(ds, donor))

    donor_diseases_new_ids = set([d.id for d in donor_diseases_new if d is not None])

    # Delete existing donor diseases that are not present in new data

    to_delete = donor_diseases_old_ids - donor_diseases_new_ids

    for donor_disease in [cd for cd in donor_diseases_old if cd.id in to_delete]:
        logger.info('Deleting obsolete donor disease %s' % donor_disease)
        donor_disease.delete()


@inject_valuef
def parse_donor_disease(valuef, source, donor):

    disease = parse_disease(source)

    if disease is not None:

        donor_disease, created = DonorDisease.objects.update_or_create(
            donor=donor,
            disease=disease,
            disease_not_normalised=valuef('other'),
            defaults={
                'primary_disease': valuef('primary', 'bool'),
                'disease_stage': valuef('stage'),
                'affected_status': valuef('affected'),
                'carrier': valuef('carrier'),
                'notes': valuef('free_text'),
            }
        )

        # Process disease variants. Create new ones, update existing with new data and delete variants that are no longer in hPSCreg data

        disease_variants_old = list(donor_disease.donor_disease_variants.all().order_by('id'))
        disease_variants_old_ids = set([v.variant_id for v in disease_variants_old])

        disease_variants_new = []

        for variant in source.get('variants', []):
            disease_variants_new.append(parse_donor_disease_variant(variant, donor_disease))

        disease_variants_new_ids = set([v.variant_id for v in disease_variants_new if v is not None])

        # Delete existing disease variants that are not present in new data

        to_delete = disease_variants_old_ids - disease_variants_new_ids

        for disease_variant in [vd for vd in disease_variants_old if vd.variant_id in to_delete]:
            logger.info('Deleting obsolete donor disease variant %s' % disease_variant)
            disease_variant.delete()

        if created:
            logger.info('Created new donor disease: %s' % disease)

        return donor_disease

    else:
        return None


@inject_valuef
def parse_donor_disease_variant(valuef, source, donor_disease):

    if valuef('gene') is not None:
        gene = parse_gene(valuef('gene'))
    else:
        gene = None

    donor_disease_variant, created = DonorDiseaseVariant.objects.update_or_create(
        donor_disease=donor_disease,
        variant_id=valuef('id'),
        defaults={
            'gene': gene,
            'chromosome_location': valuef('chromosome_location'),
            'nucleotide_sequence_hgvs': valuef('nucleotide_sequence_hgvs'),
            'protein_sequence_hgvs': valuef('protein_sequence_hgvs'),
            'zygosity_status': valuef('zygosity_status'),
            'clinvar_id': valuef('clinvar_id'),
            'dbsnp_id': valuef('dbsnp_id'),
            'dbvar_id': valuef('dbvar_id'),
            'publication_pmid': valuef('publication_pmid'),
            'notes': valuef('free_text'),
        }
    )

    if created:
        logger.info('Created new donor disease variant: %s, gene: %s' % (donor_disease_variant, donor_disease_variant.gene))

    return donor_disease_variant


@inject_valuef
def parse_gene(valuef, source):

    name = valuef('name')
    kind = 'gene'
    catalog = valuef('database_name')
    catalog_id = valuef('database_id')

    return get_or_create_molecule(name, kind, catalog, catalog_id)


@inject_valuef
def parse_disease(valuef, source):

    if not valuef('purl'):
        logger.warn('Missing disease purl')
        return None

    # Update or create the disease

    if valuef('synonyms') is None:
        synonyms = []
    else:
        synonyms = valuef('synonyms')

    disease, created = Disease.objects.update_or_create(
        xpurl=valuef('purl'),
        defaults={
            'name': valuef('purl_name'),
            'synonyms': ', '.join(synonyms),
        }
    )

    if created:
        logger.info('Created new disease: %s' % disease)

    return disease


# -----------------------------------------------------------------------------
# Genetic modifications not associated with diseases

@inject_valuef
def parse_genetic_modifications_non_disease(valuef, source, cell_line):

    if valuef('genetic_modifications_non_disease') is not None:

        genetic_modification_types = (
            ('variants_old', 'variants_old_ids', 'variants_new', 'variants_new_ids', 'Variant'),
            ('isogenic_old', 'isogenic_old_ids', 'isogenic_new', 'isogenic_new_ids', 'Isogenic modification'),
            ('transgene_old', 'transgene_old_ids', 'transgene_new', 'transgene_new_ids', 'Transgene expression'),
            ('knockout_old', 'knockout_old_ids', 'knockout_new', 'knockout_new_ids', 'Gene knock-out'),
            ('knockin_old', 'knockin_old_ids', 'knockin_new', 'knockin_new_ids', 'Gene knock-in'),
        )

        for (list_old, list_old_ids, list_new, list_new_ids, modification_type) in genetic_modification_types:
            list_old = []

            # Process disease variants. Create new ones, update existing with new data and delete variants that are no longer in hPSCreg data

            if modification_type == 'Variant':
                list_old = list(cell_line.genetic_modification_cellline_variants.all().order_by('id'))
                list_old_ids = set([v.modification_id for v in list_old])
            elif modification_type == 'Isogenic modification':
                list_old = list(cell_line.genetic_modification_cellline_isogenic.all().order_by('id'))
                list_old_ids = set([v.modification_id for v in list_old])
            elif modification_type == 'Transgene expression':
                list_old = list(cell_line.genetic_modification_cellline_transgene_expression.all().order_by('id'))
                list_old_ids = set([v.modification_id for v in list_old])
            elif modification_type == 'Gene knock-out':
                list_old = list(cell_line.genetic_modification_cellline_gene_knock_out .all().order_by('id'))
                list_old_ids = set([v.modification_id for v in list_old])
            elif modification_type == 'Gene knock-in':
                list_old = list(cell_line.genetic_modification_cellline_gene_knock_in.all().order_by('id'))
                list_old_ids = set([v.modification_id for v in list_old])

            list_new = []

            for modification in source.get('genetic_modifications_non_disease', []):
                if modification["type"] == modification_type:
                    list_new.append(parse_genetic_modification(modification, cell_line))

            # Delete existing disease variants that are not present in new data

            list_new_ids = set([v.modification_id for v in list_new if v is not None])
            to_delete = list_old_ids - list_new_ids

            for genetic_modification in [vd for vd in list_old if vd.modification_id in to_delete]:
                logger.info('Deleting obsolete genetic modification %s' % genetic_modification)
                genetic_modification.delete()

        if (list_new != list_old):
            return True
        else:
            return False

    else:
        return False


@inject_valuef
def parse_genetic_modification(valuef, source, cell_line):

    if valuef('gene') is not None:
        gene = parse_gene(valuef('gene'))
    else:
        gene = None

    if valuef('transgene') is not None:
        transgene = parse_gene(valuef('transgene'))
    else:
        transgene = None

    virus = None

    if valuef('delivery_method_virus') == 'Other' and valuef('delivery_method_virus_other') is not None:
        virus = term_list_value_of_json(source, 'delivery_method_virus_other', Virus)
    elif valuef('delivery_method_virus') is not None:
        virus = term_list_value_of_json(source, 'delivery_method_virus', Virus)

    transposon = None

    if valuef('delivery_method_transposon_type') == 'Other' and valuef('delivery_method_transposon_type_other') is not None:
        transposon = term_list_value_of_json(source, 'delivery_method_transposon_type_other', Transposon)
    elif valuef('delivery_method_transposon_type') is not None:
        transposon = term_list_value_of_json(source, 'delivery_method_transposon_type', Transposon)

    delivery_method = None

    if valuef('delivery_method') == 'Other' and valuef('delivery_method_other') is not None:
        delivery_method = valuef('delivery_method_other')
    elif valuef('delivery_method') is not None:
        delivery_method = valuef('delivery_method')

    isogenic_modificaton_type = None

    if valuef('isogenic_change_type') == 'Other' and valuef('isogenic_change_type_other') is not None:
        isogenic_modificaton_type = valuef('isogenic_change_type_other')
    elif valuef('isogenic_change_type') is not None:
        isogenic_modificaton_type = valuef('isogenic_change_type')

    if valuef('type') == 'Variant':

        cell_line_genetic_modification, created = ModificationVariantNonDisease.objects.update_or_create(
            cell_line=cell_line,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'nucleotide_sequence_hgvs': valuef('nucleotide_sequence_hgvs'),
                'protein_sequence_hgvs': valuef('protein_sequence_hgvs'),
                'zygosity_status': valuef('zygosity_status'),
                'clinvar_id': valuef('clinvar_id'),
                'dbsnp_id': valuef('dbsnp_id'),
                'dbvar_id': valuef('dbvar_id'),
                'publication_pmid': valuef('publication_pmid'),
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new genetic modification: %s , gene: %s' % (cell_line_genetic_modification, gene))

    elif valuef('type') == 'Isogenic modification':

        cell_line_genetic_modification, created = ModificationIsogenicNonDisease.objects.update_or_create(
            cell_line=cell_line,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'nucleotide_sequence_hgvs': valuef('nucleotide_sequence_hgvs'),
                'protein_sequence_hgvs': valuef('protein_sequence_hgvs'),
                'zygosity_status': valuef('zygosity_status'),
                'modification_type': isogenic_modificaton_type,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new genetic modification: %s , gene: %s' % (cell_line_genetic_modification, gene))

    elif valuef('type') == 'Transgene expression':

        cell_line_genetic_modification, created = ModificationTransgeneExpressionNonDisease.objects.update_or_create(
            cell_line=cell_line,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new genetic modification: %s , gene: %s' % (cell_line_genetic_modification, gene))

    elif valuef('type') == 'Gene knock-out':

        cell_line_genetic_modification, created = ModificationGeneKnockOutNonDisease.objects.update_or_create(
            cell_line=cell_line,
            modification_id=valuef('id'),
            defaults={
                'gene': gene,
                'chromosome_location': valuef('chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new genetic modification: %s , gene: %s' % (cell_line_genetic_modification, gene))

    elif valuef('type') == 'Gene knock-in':

        cell_line_genetic_modification, created = ModificationGeneKnockInNonDisease.objects.update_or_create(
            cell_line=cell_line,
            modification_id=valuef('id'),
            defaults={
                'target_gene': gene,
                'transgene': transgene,
                'chromosome_location': valuef('chromosome_location'),
                'chromosome_location_transgene': valuef('transgene_chromosome_location'),
                'delivery_method': delivery_method,
                'virus': virus,
                'transposon': transposon,
                'notes': valuef('free_text'),
            }
        )

        if created:
            logger.info('Added new genetic modification: %s , gene: %s' % (cell_line_genetic_modification, gene))

    else:

        return None

    return cell_line_genetic_modification


@inject_valuef
def parse_cell_type(valuef, source):

    value = valuef('primary_celltype_name')

    if value is None:
        return

    try:
        cell_type, created = CellType.objects.update_or_create(
            name=value,
            defaults={
                'purl': valuef('primary_celltype_ont_id'),
            }
        )
    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

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
def parse_derived_from(valuef, source):

    if valuef(['subclone_of', 'id']) is not None:
        try:
            return Cellline.objects.get(hescreg_id=valuef(['subclone_of', 'id']))

        except Cellline.DoesNotExist:
            return None

    else:
        return None


@inject_valuef
def parse_comparator_line(valuef, source):

    if valuef('comparator_cell_line_type') == 'Comparator line' and valuef('comparator_cell_line_id') is not None:
        try:
            return Cellline.objects.get(hescreg_id=valuef('comparator_cell_line_id'))

        except Cellline.DoesNotExist:
            return None

    else:
        return None


@inject_valuef
def parse_reprogramming_vector(valuef, source, cell_line):

    if valuef('vector_type') == 'Integrating':
        try:
            v = CelllineNonIntegratingVector.objects.get(cell_line=cell_line)
            v.delete()
            return True
        except CelllineNonIntegratingVector.DoesNotExist:
            pass
        return parse_integrating_vector(source, cell_line)

    elif valuef('vector_type') == 'Non-integrating':
        try:
            v = CelllineIntegratingVector.objects.get(cell_line=cell_line)
            v.delete()
            return True
        except CelllineIntegratingVector.DoesNotExist:
            pass
        return parse_non_integrating_vector(source, cell_line)

    else:
        return False


@inject_valuef
def parse_integrating_vector(valuef, source, cell_line):

    if valuef('integrating_vector') == 'Other':
        if valuef('integrating_vector_other') is not None:
            vector_name = valuef('integrating_vector_other')
        else:
            vector_name = u'Other'
    else:
        vector_name = valuef('integrating_vector')

    if vector_name is None:
        logger.warn('Missing name for integrating reprogramming vector')
        return False

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


@inject_valuef
def parse_non_integrating_vector(valuef, source, cell_line):

    if valuef('non_integrating_vector') == 'Other':
        if valuef('non_integrating_vector_other') is not None:
            vector_name = valuef('non_integrating_vector_other')
        else:
            vector_name = u'Other'
    else:
        vector_name = valuef('non_integrating_vector')

    if vector_name is None:
        logger.warn('Missing name for non integrating reprogramming vector')
        return False

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


def parse_vector_free_reprogramming_factor(factor):

    factor, created = VectorFreeReprogrammingFactor.objects.get_or_create(name=factor)

    if created:
        logger.info('Created new vector free reprogramming factor: %s' % factor)

    return factor


@inject_valuef
def parse_vector_free_reprogramming_factors(valuef, source, cell_line):

    if valuef('vector_free_types') is not None and valuef('vector_free_types'):
        cell_line_vector_free_reprogramming_factors, cell_line_vector_free_reprogramming_factors_created = CelllineVectorFreeReprogrammingFactors.objects.get_or_create(cell_line=cell_line)

        dirty = [cell_line_vector_free_reprogramming_factors.is_dirty(check_relationship=True)]

        for factor in [parse_vector_free_reprogramming_factor(f) for f in source.get('vector_free_types', [])]:
            cell_line_vector_free_reprogramming_factors.factors.add(factor)

        if True in dirty:
            try:
                cell_line_vector_free_reprogramming_factors.save()

                if cell_line_vector_free_reprogramming_factors_created:
                    logger.info('Added cell line vector free reprogramming factors: %s' % cell_line_vector_free_reprogramming_factors)
                else:
                    logger.info('Updated cell line vector free reprogramming factors: %s' % cell_line_vector_free_reprogramming_factors)

                return True

            except IntegrityError, e:
                logger.warn(format_integrity_error(e))
                return None

        return False


def parse_molecule(molecule_string):

    (catalog_id, name, catalog, kind) = re.split(r'###', molecule_string)

    return get_or_create_molecule(name, kind, catalog, catalog_id)


class InvalidMoleculeDataException(Exception):
    pass


def get_or_create_molecule(name, kind, catalog, catalog_id):

    kind_map = {
        'id_type_gene': 'gene',
        'gene': 'gene',
        'id_type_protein': 'protein',
        'protein': 'protein'
    }

    catalog_map = {
        'entrez_id': 'entrez',
        'entrez': 'entrez',
        'ensembl_id': 'ensembl',
        'ensembl': 'ensembl'
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
def parse_derivation(valuef, source, cell_line):

    cell_line_derivation, cell_line_derivation_created = CelllineDerivation.objects.get_or_create(cell_line=cell_line)

    cell_line_derivation.primary_cell_type = parse_cell_type(source)
    cell_line_derivation.primary_cell_type_not_normalised = valuef('primary_celltype_name_freetext')
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

    if valuef('passage_method') == 'other' or valuef('passage_method') == 'Other':
        if valuef('passage_method_other') is not None:
            cell_line_culture_conditions.passage_method = valuef('passage_method_other')
        else:
            cell_line_culture_conditions.passage_method = u'Other'
    else:
        cell_line_culture_conditions.passage_method = valuef('passage_method')

    if valuef('passage_method_enzymatic') == 'other' or valuef('passage_method_enzymatic') == 'Other':
        if valuef('passage_method_enzymatic_other') is not None:
            cell_line_culture_conditions.enzymatically = valuef('passage_method_enzymatic_other')
        else:
            cell_line_culture_conditions.enzymatically = u'Other'
    else:
        cell_line_culture_conditions.enzymatically = valuef('passage_method_enzymatic')

    if valuef('passage_method_enzyme_free') == 'other' or valuef('passage_method_enzyme_free') == 'Other':
        if valuef('passage_method_enzyme_free_other') is not None:
            cell_line_culture_conditions.enzyme_free = valuef('passage_method_enzyme_free_other')
        else:
            cell_line_culture_conditions.enzyme_free = u'Other'
    else:
        cell_line_culture_conditions.enzyme_free = valuef('passage_method_enzyme_free')

    cell_line_culture_conditions.o2_concentration = valuef('o2_concentration', 'int')
    cell_line_culture_conditions.co2_concentration = valuef('co2_concentration', 'int')
    cell_line_culture_conditions.passage_number_banked = valuef('passage_number_banked')
    cell_line_culture_conditions.number_of_vials_banked = valuef('number_of_vials_banked')

    if valuef('rock_inhibitor_used_at_passage_flag'):
        cell_line_culture_conditions.rock_inhibitor_used_at_passage = valuef('rock_inhibitor_used_at_passage_flag', 'extended_bool')

    if valuef('rock_inhibitor_used_at_cryo_flag'):
        cell_line_culture_conditions.rock_inhibitor_used_at_cryo = valuef('rock_inhibitor_used_at_cryo_flag', 'extended_bool')

    if valuef('rock_inhibitor_used_at_thaw_flag'):
        cell_line_culture_conditions.rock_inhibitor_used_at_thaw = valuef('rock_inhibitor_used_at_thaw_flag', 'extended_bool')

    if not valuef('culture_conditions_medium_culture_medium') == 'other':
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

    if not valuef('culture_conditions_medium_culture_medium') == 'other':

        # Culture medium supplements
        dirty += parse_supplements(cell_line_culture_conditions, valuef('culture_conditions_medium_culture_medium_supplements'))

    else:
        cell_line_culture_medium_other, created = CultureMediumOther.objects.get_or_create(cell_line_culture_conditions=cell_line_culture_conditions)

        cell_line_culture_medium_other.base = valuef('culture_conditions_medium_culture_medium_other_base')

        if valuef('culture_conditions_medium_culture_medium_other_protein_source') == 'other':
            if valuef('culture_conditions_medium_culture_medium_other_protein_source_other') is not None:
                cell_line_culture_medium_other.protein_source = valuef('culture_conditions_medium_culture_medium_other_protein_source_other')
            else:
                cell_line_culture_medium_other.protein_source = u'Other'
        else:
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


# -----------------------------------------------------------------------------
# Genotyping

@inject_valuef
def parse_karyotyping(valuef, source, cell_line):

    if valuef('karyotyping_flag', 'bool'):
        if valuef('karyotyping_method') == 'Other' or valuef('karyotyping_method') == 'other':
            if valuef('karyotyping_method_other') is not None:
                karyotype_method = valuef('karyotyping_method_other')
            else:
                karyotype_method = u'Other'
        else:
            karyotype_method = valuef('karyotyping_method')

        if valuef('karyotyping_karyotype') or valuef('karyotyping_method') or valuef('karyotyping_number_passages') or valuef('karyotyping_image_upload_file_enc'):

            cell_line_karyotype, cell_line_karyotype_created = CelllineKaryotype.objects.get_or_create(cell_line=cell_line)

            cell_line_karyotype.karyotype = valuef('karyotyping_karyotype')
            cell_line_karyotype.karyotype_method = karyotype_method
            cell_line_karyotype.passage_number = valuef('karyotyping_number_passages')

            if cell_line_karyotype.karyotype_file_enc:
                karyotype_file_current_enc = cell_line_karyotype.karyotype_file_enc
            else:
                karyotype_file_current_enc = None

            # Save or upadate a file if it exists
            if valuef('karyotyping_image_upload_file_enc'):
                cell_line_karyotype.karyotype_file_enc = value_of_file(valuef('karyotyping_image_upload_file_enc'), valuef('karyotyping_image_upload_file'), cell_line_karyotype.karyotype_file, karyotype_file_current_enc)

            # Delete old file if it is no longer in the export
            elif cell_line_karyotype.karyotype_file_enc:
                logger.info('Deleting obsolete karyotyping file %s' % cell_line_karyotype.karyotype_file)
                cell_line_karyotype.karyotype_file.delete()
                cell_line_karyotype.karyotype_file_enc = None

            if cell_line_karyotype_created or cell_line_karyotype.is_dirty():
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

        dirty = []

        if valuef('hla_i_a_all1') or valuef('hla_i_a_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='A')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_a_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_a_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_i_b_all1') or valuef('hla_i_b_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='B')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_b_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_b_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_i_c_all1') or valuef('hla_i_c_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='C')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_c_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_c_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dp_all1') or valuef('hla_ii_dp_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DP')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dp_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dp_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dm_all1') or valuef('hla_ii_dm_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DM')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dm_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dm_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_doa_all1') or valuef('hla_ii_doa_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DOA')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_doa_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_doa_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dq_all1') or valuef('hla_ii_dq_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DQ')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dq_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dq_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dr_all1') or valuef('hla_ii_dr_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DR')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dr_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dr_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]


@inject_valuef
def parse_str_fingerprinting(valuef, source, cell_line):

    if valuef('fingerprinting_flag', 'bool'):

        if valuef('fingerprinting') is None:
            return

        else:
            dirty = []

            for locus in valuef('fingerprinting'):
                (locus, allele1, allele2) = locus.split('###')

                str_fingerprinting, str_fingerprinting_created = CelllineStrFingerprinting.objects.get_or_create(cell_line=cell_line, locus=locus)

                str_fingerprinting.allele1 = allele1
                str_fingerprinting.allele2 = allele2

                if str_fingerprinting_created or str_fingerprinting.is_dirty():
                    str_fingerprinting.save()

                    dirty += [True]

            if True in dirty:
                logger.info('Modified cell STR/Fingerprinting')

                return True

            return False


# Genome analysis - Cell line
@inject_valuef
def parse_genome_analysis(valuef, source, cell_line):

    if valuef('genome_wide_analysis_flag'):

        cell_line_genome_analysis_old = list(cell_line.genome_analysis.all().order_by('id'))
        cell_line_genome_analysis_old_ids = set([d.id for d in cell_line_genome_analysis_old])

        # Parse new ones and save them

        cell_line_genome_analysis_new = []

        for analysis in source.get('genome_wide_analysis', []):
            cell_line_genome_analysis_new.append(parse_genome_analysis_item(analysis, cell_line))

        cell_line_genome_analysis_new_ids = set([a.id for a in cell_line_genome_analysis_new if a is not None])

        # Delete ones that are no longer in the export
        to_delete = cell_line_genome_analysis_old_ids - cell_line_genome_analysis_new_ids

        for genome_analysis in [ga for ga in cell_line_genome_analysis_old if ga.id in to_delete]:
            logger.info('Deleting obsolete genome analysis %s' % genome_analysis)
            genome_analysis.delete()


@inject_valuef
def parse_genome_analysis_item(valuef, source, cell_line):

    analysis_method = None

    if valuef('analysis_method'):
        if valuef('analysis_method') == 'Other':
            if valuef('analysis_method_other') is not None:
                analysis_method = valuef('analysis_method_other')
            else:
                analysis_method = u'Other'
        else:
            analysis_method = valuef('analysis_method')

        cell_line_genome_analysis, created = CelllineGenomeAnalysis.objects.update_or_create(
            cell_line=cell_line,
            analysis_method=analysis_method,
            defaults={
                'link': valuef('public_data_link'),
            }
        )

        genome_analysis_files_old = list(cell_line_genome_analysis.genome_analysis_files.all().order_by('id'))
        genome_analysis_files_old_encs = set([f.vcf_file_enc for f in genome_analysis_files_old])

        # Parse files and save them

        genome_analysis_files_new = []

        for f in source.get('uploads', []):
            genome_analysis_files_new.append(parse_genome_analysis_file(f, cell_line_genome_analysis))

        genome_analysis_files_new_encs = set(genome_analysis_files_new)

        # Delete existing files that are not present in new data

        to_delete = genome_analysis_files_old_encs - genome_analysis_files_new_encs

        for genome_analysis_file in [f for f in genome_analysis_files_old if f.vcf_file_enc in to_delete]:
            logger.info('Deleting obsolete genome analysis file %s' % genome_analysis_file)
            genome_analysis_file.vcf_file.delete()
            genome_analysis_file.delete()

        if created or cell_line_genome_analysis.is_dirty():
            if created:
                logger.info('Added cell line genome analysis')
            else:
                logger.info('Updated cell line genome analysis')

            cell_line_genome_analysis.save()

        return cell_line_genome_analysis

    else:
        return None


@inject_valuef
def parse_genome_analysis_file(valuef, source, genome_analysis):

    genome_analysis_file, created = CelllineGenomeAnalysisFile.objects.get_or_create(
        genome_analysis=genome_analysis,
        vcf_file_enc=valuef('filename_enc').split('.')[0]
    )

    genome_analysis_file.vcf_file_enc = value_of_file(valuef('url'), valuef('filename'), genome_analysis_file.vcf_file, genome_analysis_file.vcf_file_enc)

    genome_analysis_file.vcf_file_description = valuef('description')
    genome_analysis_file.save()

    return genome_analysis_file.vcf_file_enc


# Genome analysis - Donor
@inject_valuef
def parse_donor_genome_analysis(valuef, source, donor):

    if valuef('genome_wide_analysis_flag'):

        donor_genome_analysis_old = list(donor.donor_genome_analysis.all().order_by('id'))
        donor_genome_analysis_old_ids = set([d.id for d in donor_genome_analysis_old])

        # Parse new ones and save them

        donor_genome_analysis_new = []

        for analysis in source.get('genome_wide_analysis', []):
            donor_genome_analysis_new.append(parse_donor_genome_analysis_item(analysis, donor))

        donor_genome_analysis_new_ids = set([a.id for a in donor_genome_analysis_new if a is not None])

        # Delete ones that are no longer in the export
        to_delete = donor_genome_analysis_old_ids - donor_genome_analysis_new_ids

        for genome_analysis in [ga for ga in donor_genome_analysis_old if ga.id in to_delete]:
            logger.info('Deleting obsolete donor genome analysis %s' % genome_analysis)
            genome_analysis.delete()


@inject_valuef
def parse_donor_genome_analysis_item(valuef, source, donor):

    analysis_method = None

    if valuef('analysis_method'):
        if valuef('analysis_method') == 'Other':
            if valuef('analysis_method_other') is not None:
                analysis_method = valuef('analysis_method_other')
            else:
                analysis_method = u'Other'
        else:
            analysis_method = valuef('analysis_method')

        donor_genome_analysis, created = DonorGenomeAnalysis.objects.update_or_create(
            donor=donor,
            analysis_method=analysis_method,
            defaults={
                'link': valuef('public_data_link'),
            }
        )

        donor_genome_analysis_files_old = list(donor_genome_analysis.donor_genome_analysis_files.all().order_by('id'))
        donor_genome_analysis_files_old_encs = set([f.vcf_file_enc for f in donor_genome_analysis_files_old])

        # Parse files and save them

        donor_genome_analysis_files_new = []

        for f in source.get('uploads', []):
            donor_genome_analysis_files_new.append(parse_donor_genome_analysis_file(f, donor_genome_analysis))

        donor_genome_analysis_files_new_encs = set(donor_genome_analysis_files_new)

        # Delete existing files that are not present in new data

        to_delete = donor_genome_analysis_files_old_encs - donor_genome_analysis_files_new_encs

        for donor_genome_analysis_file in [f for f in donor_genome_analysis_files_old if f.vcf_file_enc in to_delete]:
            logger.info('Deleting obsolete donor genome analysis file %s' % donor_genome_analysis_file)
            donor_genome_analysis_file.vcf_file.delete()
            donor_genome_analysis_file.delete()

        if created or donor_genome_analysis.is_dirty():
            if created:
                logger.info('Added donor genome analysis')
            else:
                logger.info('Updated donor genome analysis')

            donor_genome_analysis.save()

        return donor_genome_analysis

    else:
        return None


@inject_valuef
def parse_donor_genome_analysis_file(valuef, source, genome_analysis):

    genome_analysis_file, created = DonorGenomeAnalysisFile.objects.get_or_create(
        genome_analysis=genome_analysis,
        vcf_file_enc=valuef('filename_enc').split('.')[0]
    )

    genome_analysis_file.vcf_file_enc = value_of_file(valuef('url'), valuef('filename'), genome_analysis_file.vcf_file, genome_analysis_file.vcf_file_enc)

    genome_analysis_file.vcf_file_description = valuef('description')
    genome_analysis_file.save()

    return genome_analysis_file.vcf_file_enc


@inject_valuef
def parse_publications(valuef, source, cell_line):

    if valuef('registration_reference_publication_pubmed_id', 'int') and valuef('registration_reference'):

        cell_line_publication, created = CelllinePublication.objects.get_or_create(cell_line=cell_line, reference_id=valuef('registration_reference_publication_pubmed_id'))

        cell_line_publication.reference_type = 'pubmed'
        cell_line_publication.reference_url = CelllinePublication.pubmed_url_from_id(valuef('registration_reference_publication_pubmed_id', 'int'))
        cell_line_publication.reference_title = valuef('registration_reference')

        if created or cell_line_publication.is_dirty():
            cell_line_publication.save()
            return True

        return False

    else:

        if CelllinePublication.objects.filter(cell_line=cell_line):
            cell_line_publication = CelllinePublication.objects.get(cell_line=cell_line)
            cell_line_publication.delete()
            return True

        else:
            return False


# Microbiology/Virology Screening
@inject_valuef
def parse_characterization(valuef, source, cell_line):

    cell_line_characterization, created = CelllineCharacterization.objects.get_or_create(cell_line=cell_line)

    certificate_of_analysis_flag = valuef('certificate_of_analysis_flag', 'nullbool')
    certificate_of_analysis_passage_number = valuef('certificate_of_analysis_passage_number')

    virology_screening_flag = valuef('virology_screening_flag', 'nullbool')
    screening_hiv1 = valuef('virology_screening_hiv_1_result')
    screening_hiv2 = valuef('virology_screening_hiv_2_result')
    screening_hepatitis_b = valuef('virology_screening_hbv_result')
    screening_hepatitis_c = valuef('virology_screening_hcv_result')
    screening_mycoplasma = valuef('virology_screening_mycoplasma_result')

    if len([x for x in (certificate_of_analysis_flag, certificate_of_analysis_passage_number, virology_screening_flag, screening_hiv1, screening_hiv2, screening_hepatitis_b, screening_hepatitis_c, screening_mycoplasma) if x is not None]):
        cell_line_characterization.certificate_of_analysis_flag = certificate_of_analysis_flag
        cell_line_characterization.certificate_of_analysis_passage_number = certificate_of_analysis_passage_number
        cell_line_characterization.virology_screening_flag = virology_screening_flag
        cell_line_characterization.screening_hiv1 = screening_hiv1
        cell_line_characterization.screening_hiv2 = screening_hiv2
        cell_line_characterization.screening_hepatitis_b = screening_hepatitis_b
        cell_line_characterization.screening_hepatitis_c = screening_hepatitis_c
        cell_line_characterization.screening_mycoplasma = screening_mycoplasma

    if created or cell_line_characterization.is_dirty():
        if created:
            logger.info('Added cell line characterization: %s' % cell_line_characterization)
        else:
            logger.info('Updated cell line characterization: %s' % cell_line_characterization)

        cell_line_characterization.save()

        return True

    return False


# Pluritest
@inject_valuef
def parse_characterization_pluritest(valuef, source, cell_line):

    if valuef('characterisation_pluritest_flag'):
        cell_line_characterization_pluritest, created = CelllineCharacterizationPluritest.objects.get_or_create(cell_line=cell_line)

        cell_line_characterization_pluritest.pluritest_flag = valuef('characterisation_pluritest_flag', 'nullbool')
        cell_line_characterization_pluritest.pluripotency_score = valuef(['characterisation_pluritest_data', 'pluripotency_score'])
        cell_line_characterization_pluritest.novelty_score = valuef(['characterisation_pluritest_data', 'novelty_score'])
        cell_line_characterization_pluritest.microarray_url = valuef(['characterisation_pluritest_data', 'microarray_url'])

        # Parse files and save them

        characterization_pluritest_files_old = list(cell_line_characterization_pluritest.pluritest_files.all().order_by('id'))
        characterization_pluritest_files_old_encs = set([f.file_enc for f in characterization_pluritest_files_old])

        characterization_pluritest_files_new = []

        for f in valuef(['characterisation_pluritest_data']).get('uploads', []):
            characterization_pluritest_files_new.append(parse_characterization_pluritest_file(f, cell_line_characterization_pluritest))

        characterization_pluritest_files_new_encs = set(characterization_pluritest_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_pluritest_files_old_encs - characterization_pluritest_files_new_encs

        for characterization_pluritest_file in [f for f in characterization_pluritest_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete pluritest file %s' % characterization_pluritest_file)
            characterization_pluritest_file.file_doc.delete()
            characterization_pluritest_file.delete()

        if created or cell_line_characterization_pluritest.is_dirty():
            if created:
                logger.info('Added cell line characterization pluritest: %s' % cell_line_characterization_pluritest)
            else:
                logger.info('Updated cell line characterization pluritest: %s' % cell_line_characterization_pluritest)

            cell_line_characterization_pluritest.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationPluritest.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationPluritest.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_pluritest_file(valuef, source, characterization_pluritest):

    characterization_pluritest_file, created = CelllineCharacterizationPluritestFile.objects.get_or_create(
        pluritest=characterization_pluritest,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_pluritest_file.file_enc

    characterization_pluritest_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_pluritest_file.file_doc, current_enc)

    characterization_pluritest_file.file_description = valuef('description')
    characterization_pluritest_file.save()

    return characterization_pluritest_file.file_enc


# EpiPluriTest
@inject_valuef
def parse_characterization_epipluriscore(valuef, source, cell_line):

    if valuef('characterisation_epipluriscore_flag'):
        cell_line_characterization_epipluriscore, created = CelllineCharacterizationEpipluriscore.objects.get_or_create(cell_line=cell_line)

        cell_line_characterization_epipluriscore.epipluriscore_flag = valuef('characterisation_epipluriscore_flag', 'nullbool')
        cell_line_characterization_epipluriscore.score = valuef(['characterisation_epipluriscore_data', 'score'])

        if valuef(['characterisation_epipluriscore_data', 'mcpg_present_flag']) == '1':
            marker_mcpg = True
        elif valuef(['characterisation_epipluriscore_data', 'mcpg_absent_flag']) == '1':
            marker_mcpg = False
        else:
            marker_mcpg = None

        if valuef(['characterisation_epipluriscore_data', 'oct4_present_flag']) == '1':
            marker_OCT4 = True
        elif valuef(['characterisation_epipluriscore_data', 'oct4_absent_flag']) == '1':
            marker_OCT4 = False
        else:
            marker_OCT4 = None

        cell_line_characterization_epipluriscore.marker_mcpg = marker_mcpg
        cell_line_characterization_epipluriscore.marker_OCT4 = marker_OCT4

        # Parse files and save them

        characterization_epipluriscore_files_old = list(cell_line_characterization_epipluriscore.epipluriscore_files.all().order_by('id'))
        characterization_epipluriscore_files_old_encs = set([f.file_enc for f in characterization_epipluriscore_files_old])

        characterization_epipluriscore_files_new = []

        for f in valuef(['characterisation_epipluriscore_data']).get('uploads', []):
            characterization_epipluriscore_files_new.append(parse_characterization_epipluriscore_file(f, cell_line_characterization_epipluriscore))

        characterization_epipluriscore_files_new_encs = set(characterization_epipluriscore_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_epipluriscore_files_old_encs - characterization_epipluriscore_files_new_encs

        for characterization_epipluriscore_file in [f for f in characterization_epipluriscore_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete epipluriscore file %s' % characterization_epipluriscore_file)
            characterization_epipluriscore_file.file_doc.delete()
            characterization_epipluriscore_file.delete()

        if created or cell_line_characterization_epipluriscore.is_dirty():
            if created:
                logger.info('Added cell line characterization EpiPluriScore: %s' % cell_line_characterization_epipluriscore)
            else:
                logger.info('Updated cell line characterization EpiPluriScore: %s' % cell_line_characterization_epipluriscore)

            cell_line_characterization_epipluriscore.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationEpipluriscore.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationEpipluriscore.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_epipluriscore_file(valuef, source, characterization_epipluriscore):

    characterization_epipluriscore_file, created = CelllineCharacterizationEpipluriscoreFile.objects.get_or_create(
        epipluriscore=characterization_epipluriscore,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_epipluriscore_file.file_enc

    characterization_epipluriscore_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_epipluriscore_file.file_doc, current_enc)

    characterization_epipluriscore_file.file_description = valuef('description')
    characterization_epipluriscore_file.save()

    return characterization_epipluriscore_file.file_enc


# Morphology images - undifferentitated cells
@inject_valuef
def parse_characterization_undiff_morphology(valuef, source, cell_line):

    if valuef('characterisation_morphology_flag'):

        # Parse files and save them

        characterization_undiff_morphology_files_old = list(cell_line.undifferentiated_morphology_files.all().order_by('id'))

        characterization_undiff_morphology_files_old_encs = set([f.file_enc for f in characterization_undiff_morphology_files_old])

        characterization_undiff_morphology_files_new = []
        characterization_undiff_morphology_files_new_encs = set([])

        if valuef('characterisation_morphology_data'):
            for f in valuef(['characterisation_morphology_data']).get('uploads', []):
                characterization_undiff_morphology_files_new.append(parse_characterization_undiff_morphology_file(f, cell_line))

            characterization_undiff_morphology_files_new_encs = set(characterization_undiff_morphology_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_undiff_morphology_files_old_encs - characterization_undiff_morphology_files_new_encs

        for characterization_undiff_morphology_file in [f for f in characterization_undiff_morphology_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete undiff morphology file %s' % characterization_undiff_morphology_file)
            characterization_undiff_morphology_file.file_doc.delete()
            characterization_undiff_morphology_file.delete()

        if characterization_undiff_morphology_files_old_encs != characterization_undiff_morphology_files_new_encs:
            logger.info('Updated cell line characterization morphology')
            return True
        else:
            return False


@inject_valuef
def parse_characterization_undiff_morphology_file(valuef, source, cell_line):

    characterization_undiff_morphology_file, created = CelllineCharacterizationUndifferentiatedMorphologyFile.objects.get_or_create(
        cell_line=cell_line,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_undiff_morphology_file.file_enc

    characterization_undiff_morphology_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_undiff_morphology_file.file_doc, current_enc)

    characterization_undiff_morphology_file.file_description = valuef('description')
    characterization_undiff_morphology_file.save()

    return characterization_undiff_morphology_file.file_enc


# hPSC Scorecard
@inject_valuef
def parse_characterization_hpscscorecard(valuef, source, cell_line):

    if valuef('characterisation_hpsc_scorecard_flag') and valuef('characterisation_hpsc_scorecard_data'):
        cell_line_characterization_hpscscorecard, created = CelllineCharacterizationHpscScorecard.objects.get_or_create(cell_line=cell_line)

        if valuef(['characterisation_hpsc_scorecard_data', 'self_renewal_flag']) == '1':
            self_renewal = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'self_renewal_flag']) == '0':
            self_renewal = False
        else:
            self_renewal = None

        cell_line_characterization_hpscscorecard.self_renewal = self_renewal

        if valuef(['characterisation_hpsc_scorecard_data', 'endoderm_flag']) == '1':
            endoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'endoderm_flag']) == '0':
            endoderm = False
        else:
            endoderm = None

        cell_line_characterization_hpscscorecard.endoderm = endoderm

        if valuef(['characterisation_hpsc_scorecard_data', 'mesoderm_flag']) == '1':
            mesoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'mesoderm_flag']) == '0':
            mesoderm = False
        else:
            mesoderm = None

        cell_line_characterization_hpscscorecard.mesoderm = mesoderm

        if valuef(['characterisation_hpsc_scorecard_data', 'ectoderm_flag']) == '1':
            ectoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'ectoderm_flag']) == '0':
            ectoderm = False
        else:
            ectoderm = None

        cell_line_characterization_hpscscorecard.ectoderm = ectoderm

        # Parse files and save them

        # Data files
        characterization_hpscscorecard_files_old = list(cell_line_characterization_hpscscorecard.hpsc_scorecard_reports.all().order_by('id'))
        characterization_hpscscorecard_files_old_encs = set([f.file_enc for f in characterization_hpscscorecard_files_old])

        characterization_hpscscorecard_files_new = []

        for f in valuef(['characterisation_hpsc_scorecard_data']).get('data_analysis_uploads', []):
            characterization_hpscscorecard_files_new.append(parse_characterization_hpscscorecard_file(f, cell_line_characterization_hpscscorecard))

        characterization_hpscscorecard_files_new_encs = set(characterization_hpscscorecard_files_new)

        # Scorecards
        characterization_hpscscorecard_cards_old = list(cell_line_characterization_hpscscorecard.hpsc_scorecard_files.all().order_by('id'))
        characterization_hpscscorecard_cards_old_encs = set([f.file_enc for f in characterization_hpscscorecard_cards_old])

        characterization_hpscscorecard_cards_new = []

        for f in valuef(['characterisation_hpsc_scorecard_data']).get('scorecard_uploads', []):
            characterization_hpscscorecard_cards_new.append(parse_characterization_hpscscorecard_card(f, cell_line_characterization_hpscscorecard))

        characterization_hpscscorecard_cards_new_encs = set(characterization_hpscscorecard_cards_new)

        # Delete existing files that are not present in new data

        # Data files
        to_delete = characterization_hpscscorecard_files_old_encs - characterization_hpscscorecard_files_new_encs

        for characterization_hpscscorecard_file in [f for f in characterization_hpscscorecard_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete hPSC Scorecard data file %s' % characterization_hpscscorecard_file)
            characterization_hpscscorecard_file.file_doc.delete()
            characterization_hpscscorecard_file.delete()

        # hPSC Scorecards files
        to_delete = characterization_hpscscorecard_cards_old_encs - characterization_hpscscorecard_cards_new_encs

        for characterization_hpscscorecard_card in [f for f in characterization_hpscscorecard_cards_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete hPSC Scorecard %s' % characterization_hpscscorecard_card)
            characterization_hpscscorecard_card.file_doc.delete()
            characterization_hpscscorecard_card.delete()

        # Save

        if created or cell_line_characterization_hpscscorecard.is_dirty():
            if created:
                logger.info('Added cell line characterization hPSC Scorecard: %s' % cell_line_characterization_hpscscorecard)
            else:
                logger.info('Updated cell line characterization hPSC Scorecard: %s' % cell_line_characterization_hpscscorecard)

            cell_line_characterization_hpscscorecard.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationHpscScorecard.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationHpscScorecard.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_hpscscorecard_file(valuef, source, characterization_hpscscorecard):

    characterization_hpscscorecard_file, created = CelllineCharacterizationHpscScorecardReport.objects.get_or_create(
        hpsc_scorecard=characterization_hpscscorecard,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_hpscscorecard_file.file_enc

    characterization_hpscscorecard_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_hpscscorecard_file.file_doc, current_enc)

    characterization_hpscscorecard_file.file_description = valuef('description')
    characterization_hpscscorecard_file.save()

    return characterization_hpscscorecard_file.file_enc


@inject_valuef
def parse_characterization_hpscscorecard_card(valuef, source, characterization_hpscscorecard):

    characterization_hpscscorecard_card, created = CelllineCharacterizationHpscScorecardScorecard.objects.get_or_create(
        hpsc_scorecard=characterization_hpscscorecard,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_hpscscorecard_card.file_enc

    characterization_hpscscorecard_card.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_hpscscorecard_card.file_doc, current_enc)

    characterization_hpscscorecard_card.file_description = valuef('description')
    characterization_hpscscorecard_card.save()

    return characterization_hpscscorecard_card.file_enc


@inject_valuef
def parse_characterization_marker_expression(valuef, source, cell_line):

    cell_line_marker_expressions_old = list(cell_line.undifferentiated_marker_expression.all().order_by('marker_id'))
    cell_line_marker_expressions_old_ids = set([m.marker_id for m in cell_line_marker_expressions_old])

    # Parse marker expressions and save them

    cell_line_marker_expressions_new = []

    for marker in source.get('characterisation_marker_expression_data', []):
        cell_line_marker_expressions_new.append(parse_marker_expression(marker, cell_line))

    cell_line_marker_expressions_new_ids = set([m.marker_id for m in cell_line_marker_expressions_new if m is not None])

    # Delete existing marker expressions that are not present in new data

    to_delete = cell_line_marker_expressions_old_ids - cell_line_marker_expressions_new_ids

    for cell_line_marker_expression in [me for me in cell_line_marker_expressions_old if me.marker_id in to_delete]:
        logger.info('Deleting obsolete cell line marker expression %s' % cell_line_marker_expression)
        cell_line_marker_expression.delete()

    # Check for changes (dirty)

    if (cell_line_marker_expressions_old_ids != cell_line_marker_expressions_new_ids):
        return True

    # TODO - add checking for updates once hPSCreg export is fixed
    # else:
    #     def marker_expressions_equal(a, b):
    #         return (
    #             a.marker_id == b.marker_id and
    #             a.marker == b.marker and
    #             a.expressed == b.expressed
    #         )
    #     for (old, new) in zip(cell_line_marker_expressions_old, cell_line_marker_expressions_new):
    #         if not marker_expressions_equal(old, new):
    #             return True

    return False


@inject_valuef
def parse_marker_expression(valuef, source, cell_line):

    if valuef('marker') is not None and valuef('marker_id') is not None:
        marker_id = valuef('marker_id')
        marker_name = valuef('marker').get('name')

        if valuef('expressed') == '1':
            marker_expressed_flag = True
        elif valuef('not_expressed') == '1':
            marker_expressed_flag = False
        else:
            marker_expressed_flag = None

        cell_line_marker_expression, created = CelllineCharacterizationMarkerExpression.objects.update_or_create(
            cell_line=cell_line,
            marker_id=marker_id,
            marker=marker_name,
            defaults={
                'expressed': marker_expressed_flag,
            }
        )

        for method in source.get('methods', []):
            parse_marker_expression_method(method, cell_line_marker_expression)

        # TODO - add checking for updates once hPSCreg export is fixed
        # list_old = list(cell_line_marker_expression.marker_expression_method.all().order_by('id'))
        # list_old_ids = set([m.id for m in list_old])
        #
        # list_new = []
        #
        # for method in source.get('methods', []):
        #     list_new.append(parse_marker_expression_method(method, cell_line_marker_expression))
        #
        # list_new_ids = set([m.id for m in list_new if m is not None])

        # Delete existing disease variants that are not present in new data

        # to_delete = list_old_ids - list_new_ids
        #
        # for marker_expression_method in [m for m in list_old if m.id in to_delete]:
        #     logger.info('Deleting obsolete marker expression method %s' % marker_expression_method)
        #     marker_expression_method.delete()

        if created:
            logger.info('Created new cell line marker expression: %s' % cell_line_marker_expression)

        return cell_line_marker_expression

    else:
        return None


@inject_valuef
def parse_marker_expression_method(valuef, source, cell_line_marker_expression):

    if valuef('name') is not None:

        cell_line_marker_expression_method, created = CelllineCharacterizationMarkerExpressionMethod.objects.update_or_create(
            marker_expression=cell_line_marker_expression,
            name=valuef('name'),
        )

        # Parse files and save them

        method_files_old = list(cell_line_marker_expression_method.marker_expression_method_files.all().order_by('id'))
        method_files_old_encs = set([f.file_enc for f in method_files_old])

        method_files_new = []
        method_files_new_encs = set()

        if valuef('uploads'):
            for f in valuef('uploads'):
                method_files_new.append(parse_marker_expression_method_file(f, cell_line_marker_expression_method))

            method_files_new_encs = set(method_files_new)

        # Delete existing files that are not present in new data

        to_delete = method_files_old_encs - method_files_new_encs

        for method_file in [f for f in method_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete marker method file %s' % method_file)
            method_file.file_doc.delete()
            method_file.delete()

        if created:
            logger.info('Created new cell line marker expression method: %s' % cell_line_marker_expression_method)

        return cell_line_marker_expression_method

    else:
        return None


@inject_valuef
def parse_marker_expression_method_file(valuef, source, cell_line_marker_expression_method):

    marker_method_file, created = CelllineCharacterizationMarkerExpressionMethodFile.objects.get_or_create(
        marker_expression_method=cell_line_marker_expression_method,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = marker_method_file.file_enc

    marker_method_file.file_enc = value_of_file(valuef('url'), valuef('filename'), marker_method_file.file_doc, current_enc)

    marker_method_file.file_description = valuef('description')
    marker_method_file.save()

    return marker_method_file.file_enc


# OLD fields
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
            marker, marker_created = marker_model.objects.get_or_create(cell_line=cell_line)

            marker.passage_number = valuef(hescreg_slug_passage_number)

            for string in valuef(hescreg_slug):
                aux_molecule_result(marker, marker_molecule_model, string)

            dirty = [marker.is_dirty(check_relationship=True)]

            if True in dirty:
                if marker_created:
                    logger.info('Added new Undifferentiated marker to cell line')
                else:
                    logger.info('Changed Undifferentiated marker of cell line')

                marker.save()

                return True

            return False

    def aux_molecule_result(marker, marker_molecule_model, string):

        if len(string.split('###')) == 2:
            (molecule_name, result) = string.split('###')
            try:
                molecule = molecule_name

                marker_molecule, marker_molecule_created = marker_molecule_model.objects.get_or_create(marker=marker, molecule=molecule)

                marker_molecule.result = result

                if marker_molecule_created or marker_molecule.is_dirty():
                    marker_molecule.save()

                    return True

                return False

            except InvalidMoleculeDataException:
                pass
        else:
            (molecule_catalog_id, result, molecule_name, molecule_catalog, molecule_kind) = string.split('###')
            try:
                # molecule = get_or_create_molecule(molecule_name, molecule_kind, molecule_catalog, molecule_catalog_id)
                molecule = molecule_name

                marker_molecule, marker_molecule_created = marker_molecule_model.objects.get_or_create(marker=marker, molecule=molecule)

                marker_molecule.result = result

                if marker_molecule_created or marker_molecule.is_dirty():
                    marker_molecule.save()

                    return True

                return False

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

        undifferentiated_morphology_marker_morphology, undifferentiated_morphology_marker_morphology_created = UndifferentiatedMorphologyMarkerMorphology.objects.get_or_create(cell_line=cell_line)

        undifferentiated_morphology_marker_morphology.passage_number = valuef('undiff_morphology_markers_passage_number')
        undifferentiated_morphology_marker_morphology.description = valuef('undiff_morphology_markers_description')
        undifferentiated_morphology_marker_morphology.data_url = valuef('undiff_morphology_markers_enc_filename')

        if undifferentiated_morphology_marker_morphology_created or undifferentiated_morphology_marker_morphology.is_dirty():
            if undifferentiated_morphology_marker_morphology_created:
                logger.info('Added cell line undifferentitated morphology marker: %s' % undifferentiated_morphology_marker_morphology)
            else:
                logger.info('Updated cell line  undifferentitated morphology marker: %s' % undifferentiated_morphology_marker_morphology)

            undifferentiated_morphology_marker_morphology.save()

            return True

        return False

    else:
        try:
            m = UndifferentiatedMorphologyMarkerMorphology.objects.get(cell_line=cell_line)
            m.delete()

            logger.info('Deleting cell line undifferentitated morphology marker')

        except UndifferentiatedMorphologyMarkerMorphology.DoesNotExist:
            return False

    # UndifferentiatedMorphologyMarkerExpressionProfile

    if any([valuef(x) for x in (
        'undiff_exprof_markers_method_name',
        'undiff_exprof_markers_weblink',
        'undiff_exprof_markers_enc_filename',
        'undiff_exprof_markers_passage_number',
    )]):

        undifferentiated_morphology_marker_expression_profile, undifferentiated_morphology_marker_expression_profile_created = UndifferentiatedMorphologyMarkerExpressionProfile.objects.get_or_create(cell_line=cell_line)

        undifferentiated_morphology_marker_expression_profile.method = valuef('undiff_exprof_markers_method_name')
        undifferentiated_morphology_marker_expression_profile.passage_number = valuef('undiff_exprof_markers_passage_number')
        undifferentiated_morphology_marker_expression_profile.data_url = valuef('undiff_exprof_markers_weblink')
        undifferentiated_morphology_marker_expression_profile.uploaded_data_url = valuef('undiff_exprof_markers_enc_filename')

        if valuef('undiff_exprof_expression_array_marker'):
            aux_molecule_result(undifferentiated_morphology_marker_expression_profile, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_expression_array_marker'))
        elif valuef('undiff_exprof_rna_sequencing_marker'):
            aux_molecule_result(undifferentiated_morphology_marker_expression_profile, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_rna_sequencing_marker'))
        elif valuef('undiff_exprof_proteomics_marker'):
            aux_molecule_result(undifferentiated_morphology_marker_expression_profile, UndifferentiatedMorphologyMarkerExpressionProfileMolecule, valuef('undiff_exprof_proteomics_marker'))

        dirty = [undifferentiated_morphology_marker_expression_profile.is_dirty(check_relationship=True)]

        if True in dirty:
            if undifferentiated_morphology_marker_expression_profile_created:
                logger.info('Added new Undifferentiated marker to cell line')
            else:
                logger.info('Changed Undifferentiated marker of cell line')

            undifferentiated_morphology_marker_expression_profile.save()

            return True

        return False


# -----------------------------------------------------------------------------
