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
    Cellline,  \
    Gender,  \
    Molecule,  \
    MoleculeReference,  \
    Virus,  \
    Transposon,  \
    Unit,  \
    Donor,  \
    DonorRelatives,  \
    DonorDisease,  \
    DonorDiseaseVariant, \
    DonorGenomeAnalysis, \
    DonorGenomeAnalysisFile, \
    Disease,  \
    CelllineDisease,  \
    CelllineCultureConditions,  \
    CultureMediumOther,  \
    CelllineCultureMediumSupplement,  \
    Organization,  \
    CelllineOrgType,  \
    CelllinePublication,  \
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

    if os.getenv("TOMCAT_URL"):
        server = os.getenv("TOMCAT_URL").split("/")[2].split(":")[0]

    if "hpscreg.local" in source_file_link and server:
        source_file_link = source_file_link.replace("hpscreg.local", server)
    if "localhost" in source_file_link and server:
        source_file_link = source_file_link.replace("localhost", server)

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

    parse_donor_relatives(source, donor)
    parse_donor_diseases(source, donor)
    parse_donor_genome_analysis(source, donor)

    return donor


# -----------------------------------------------------------------------------
# Donor relatives

def parse_donor_relatives(source, donor):

    donor_relatives_old = list(donor.relatives.all().order_by('related_donor__biosamples_id'))
    donor_relatives_old_ids = set([r.related_donor.biosamples_id for r in donor_relatives_old])

    donor_relatives_new_ids = []

    for relative in source.get('relatives', []):
        donor_relatives_new_ids.append(parse_donor_relative(relative, donor))

    # Delete existing donor relatives that are not present in new data
    to_delete = donor_relatives_old_ids - set(donor_relatives_new_ids)

    for donor_relative in [r for r in donor_relatives_old if r.related_donor.biosamples_id in to_delete]:
        logger.info('Deleting obsolete donor relative %s' % donor_relative)
        donor_relative.delete()


@inject_valuef
def parse_donor_relative(valuef, source, donor):

    # Save relation if relative exists in IMS
    try:
        relative = Donor.objects.get(biosamples_id=valuef('biosamples_id'))

        donor_relative, created = DonorRelatives.objects.update_or_create(
            donor=donor,
            related_donor=relative,
            defaults={
                'relation': valuef('type'),
            }
        )

        if created or donor_relative.is_dirty():
            if created:
                logger.info('Added new donor relative %s' % donor_relative)
            else:
                logger.info('Updated donor  relative %s' % donor_relative)

        return relative.biosamples_id

    except Donor.DoesNotExist:
        return None


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
        try:
            reference, created = MoleculeReference.objects.get_or_create(molecule=molecule, catalog=catalog, catalog_id=catalog_id)
        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            pass

        if created:
            logger.info('Created new molecule reference: %s' % reference)

    return molecule


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
