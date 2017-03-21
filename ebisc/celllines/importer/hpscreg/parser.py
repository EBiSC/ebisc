import re
import functools

import logging
logger = logging.getLogger('management.commands')

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
    CelllineCharacterizationPluritest, \
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
    CelllineDiseaseGenotype, \
    CelllineGenotypingSNP, \
    CelllineGenotypingRsNumber, \
    CelllineHlaTyping, \
    CelllineStrFingerprinting, \
    CelllineGenomeAnalysis, \
    ModificationVariantDisease, \
    ModificationVariantNonDisease, \
    ModificationIsogenicDisease, \
    ModificationIsogenicNonDisease, \
    ModificationTransgeneExpressionDisease, \
    ModificationTransgeneExpressionNonDisease, \
    ModificationGeneKnockOutDisease, \
    ModificationGeneKnockOutNonDisease, \
    ModificationGeneKnockInDisease, \
    ModificationGeneKnockInNonDisease, \
    CelllineGeneticModification, \
    GeneticModificationTransgeneExpression, \
    GeneticModificationGeneKnockOut, \
    GeneticModificationGeneKnockIn, \
    GeneticModificationIsogenic


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
# Specific parsers

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
        )

        try:
            donor.save()
        except IntegrityError, e:
            logger.warn(format_integrity_error(e))
            return None

    parse_donor_diseases(source, donor)

    return donor


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

    if valuef('same_donor_derived_from_cell_line_id') is not None:
        try:
            return Cellline.objects.get(hescreg_id=valuef('same_donor_derived_from_cell_line_id'))

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

        if valuef('karyotyping_karyotype') or valuef('karyotyping_method') or valuef('karyotyping_number_passages'):

            cell_line_karyotype, cell_line_karyotype_created = CelllineKaryotype.objects.get_or_create(cell_line=cell_line)

            cell_line_karyotype.karyotype = valuef('karyotyping_karyotype')
            cell_line_karyotype.karyotype_method = karyotype_method
            cell_line_karyotype.passage_number = valuef('karyotyping_number_passages')

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


@inject_valuef
def parse_genome_analysis(valuef, source, cell_line):

    if valuef('genome_wide_genotyping_flag', 'bool'):

        data_type = None

        if valuef('genome_wide_genotyping_ega'):
            if valuef('genome_wide_genotyping_ega') == 'Other':
                if valuef('genome_wide_genotyping_ega_other') is not None:
                    data_type = valuef('genome_wide_genotyping_ega_other')
                else:
                    data_type = u'Other'
            else:
                data_type = valuef('genome_wide_genotyping_ega')

        if data_type or valuef('genome_wide_genotyping_ega_url'):

            cell_line_genome_analysis, cell_line_genome_analysis_created = CelllineGenomeAnalysis.objects.get_or_create(cell_line=cell_line)

            cell_line_genome_analysis.data = data_type
            cell_line_genome_analysis.link = valuef('genome_wide_genotyping_ega_url')

            if cell_line_genome_analysis_created or cell_line_genome_analysis.is_dirty():
                if cell_line_genome_analysis_created:
                    logger.info('Added cell line genome analysis')
                else:
                    logger.info('Updated cell line genome analysis')

                cell_line_genome_analysis.save()

                return True

            return False


@inject_valuef
def parse_genetic_modifications(valuef, source, cell_line):

    if valuef('genetic_modification_flag') is not None:

        dirty_genetic_modification = []

        genetic_modification, genetic_modification_created = CelllineGeneticModification.objects.get_or_create(cell_line=cell_line)

        genetic_modification.genetic_modification_flag = valuef('genetic_modification_flag', 'nullbool')
        genetic_modification.types = valuef('genetic_modification_types')

        if genetic_modification_created or genetic_modification.is_dirty():
            if genetic_modification_created:
                logger.info('Added cell line genetic modification')
            else:
                logger.info('Updated cell line genetic modification')

            genetic_modification.save()
            dirty_genetic_modification += [True]

        if valuef('genetic_modification_types') is not None:

            def parse_delivery_method(source, source_field, source_field_other):

                if source_field not in source and source_field_other not in source:
                    return None

                delivery_method = None

                if valuef(source_field) == 'Other':
                    if valuef(source_field_other) is not None:
                        delivery_method = valuef(source_field_other)
                    else:
                        delivery_method = u'Other'
                else:
                    delivery_method = valuef(source_field)

                return delivery_method

            for modification_type in valuef('genetic_modification_types'):
                if modification_type == 'gen_mod_transgene_expression':

                    transgene_expression, transgene_expression_created = GeneticModificationTransgeneExpression.objects.get_or_create(cell_line=cell_line)

                    transgene_expression.delivery_method = parse_delivery_method(source, 'transgene_delivery_method', 'transgene_delivery_method_other')

                    if valuef('transgene_viral_method_spec') == 'Other':
                        if valuef('transgene_viral_method_spec_other') is not None:
                            transgene_expression.virus = term_list_value_of_json(source, 'transgene_viral_method_spec_other', Virus)
                        else:
                            transgene_expression.virus = None
                    else:
                        transgene_expression.virus = term_list_value_of_json(source, 'transgene_viral_method_spec', Virus)

                    if valuef('transgene_transposon_method_spec') == 'Other':
                        if valuef('transgene_transposon_method_spec_other') is not None:
                            transgene_expression.transposon = term_list_value_of_json(source, 'transgene_transposon_method_spec_other', Transposon)
                        else:
                            transgene_expression.transposon = None
                    else:
                        transgene_expression.transposon = term_list_value_of_json(source, 'transgene_transposon_method_spec', Transposon)

                    for gene in [parse_molecule(g) for g in source.get('genetic_modification_transgene_expression_list', [])]:
                        transgene_expression.genes.add(gene)

                    dirty = [transgene_expression.is_dirty(check_relationship=True)]

                    if True in dirty:
                        if transgene_expression_created:
                            logger.info('Added transgene expression modification: %s' % transgene_expression)
                        else:
                            logger.info('Updated transgene expression modification: %s' % transgene_expression)

                        transgene_expression.save()
                        dirty_genetic_modification += [True]

                elif modification_type == 'gen_mod_gene_knock_out':

                    gene_knock_out, gene_knock_out_created = GeneticModificationGeneKnockOut.objects.get_or_create(cell_line=cell_line)

                    gene_knock_out.delivery_method = parse_delivery_method(source, 'knockout_delivery_method', 'knockout_delivery_method_other')

                    if valuef('knockout_viral_method_spec') == 'Other':
                        if valuef('knockout_viral_method_spec_other') is not None:
                            gene_knock_out.virus = term_list_value_of_json(source, 'knockout_viral_method_spec_other', Virus)
                        else:
                            gene_knock_out.virus = None
                    else:
                        gene_knock_out.virus = term_list_value_of_json(source, 'knockout_viral_method_spec', Virus)

                    if valuef('knockout_transposon_method_spec') == 'Other':
                        if valuef('knockout_transposon_method_spec_other') is not None:
                            gene_knock_out.transposon = term_list_value_of_json(source, 'knockout_transposon_method_spec_other', Transposon)
                        else:
                            gene_knock_out.transposon = u'Other'
                    else:
                        gene_knock_out.transposon = term_list_value_of_json(source, 'knockout_transposon_method_spec', Transposon)

                    for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockout_list', [])]:
                        gene_knock_out.target_genes.add(gene)

                    dirty = [gene_knock_out.is_dirty(check_relationship=True)]

                    if True in dirty:
                        if gene_knock_out_created:
                            logger.info('Added gene knock-out modification: %s' % gene_knock_out)
                        else:
                            logger.info('Updated gene knock-out modification: %s' % gene_knock_out)

                        gene_knock_out.save()
                        dirty_genetic_modification += [True]

                elif modification_type == 'gen_mod_gene_knock_in':

                    gene_knock_in, gene_knock_in_created = GeneticModificationGeneKnockIn.objects.get_or_create(cell_line=cell_line)

                    gene_knock_in.delivery_method = parse_delivery_method(source, 'knockin_delivery_method', 'knockin_delivery_method_other')

                    if valuef('knockin_viral_method_spec') == 'Other':
                        if valuef('knockin_viral_method_spec_other') is not None:
                            gene_knock_in.virus = term_list_value_of_json(source, 'knockin_viral_method_spec_other', Virus)
                        else:
                            gene_knock_in.virus = None
                    else:
                        gene_knock_in.virus = term_list_value_of_json(source, 'knockin_viral_method_spec', Virus)

                    if valuef('knockin_transposon_method_spec') == 'Other':
                        if valuef('knockin_transposon_method_spec_other') is not None:
                            gene_knock_in.transposon = term_list_value_of_json(source, 'knockin_transposon_method_spec_other', Transposon)
                        else:
                            gene_knock_in.transposon = u'Other'
                    else:
                        gene_knock_in.transposon = term_list_value_of_json(source, 'knockin_transposon_method_spec', Transposon)

                    for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockin_target_gene_list', [])]:
                        logger.info('Added gene: %s' % gene)
                        gene_knock_in.target_genes.add(gene)

                    for gene in [parse_molecule(g) for g in source.get('genetic_modification_knockin_transgene_list', [])]:
                        logger.info('Added gene: %s' % gene)
                        gene_knock_in.transgenes.add(gene)

                    dirty = [gene_knock_in.is_dirty(check_relationship=True)]

                    if True in dirty:
                        if gene_knock_in_created:
                            logger.info('Added gene knock-in modification: %s' % gene_knock_in)
                        else:
                            logger.info('Updated gene knock-in modification: %s' % gene_knock_in)

                        gene_knock_in.save()
                        dirty_genetic_modification += [True]

                elif modification_type == 'gen_mod_isogenic_modication':

                    isogenic_modification, isogenic_modification_created = GeneticModificationIsogenic.objects.get_or_create(cell_line=cell_line)

                    isogenic_modification.change_type = valuef('genetic_modification_isogenic_modified_locus_change_type')
                    isogenic_modification.modified_sequence = valuef('genetic_modification_isogenic_modified_locus')

                    for gene in [parse_molecule(g) for g in source.get('genetic_modification_isogenic_target_locus_list', [])]:
                        logger.info('Added gene: %s' % gene)
                        isogenic_modification.target_locus.add(gene)

                    dirty = [isogenic_modification.is_dirty(check_relationship=True)]

                    if True in dirty:
                        if isogenic_modification_created:
                            logger.info('Added gene isogenic modification: %s' % isogenic_modification)
                        else:
                            logger.info('Updated gene isogenic modification: %s' % isogenic_modification)

                        isogenic_modification.save()
                        dirty_genetic_modification += [True]

        if True in dirty_genetic_modification:
            logger.info('Modified genetic modification')
            return True
        else:
            return False


@inject_valuef
def parse_disease_associated_genotype(valuef, source, cell_line):

    if valuef('carries_disease_phenotype_associated_variants_flag'):

        cell_line_disease_genotype, cell_line_disease_genotype_created = CelllineDiseaseGenotype.objects.get_or_create(cell_line=cell_line)

        cell_line_disease_genotype.carries_disease_phenotype_associated_variants = valuef('carries_disease_phenotype_associated_variants_flag', 'nullbool')
        cell_line_disease_genotype.variant_of_interest = valuef('variant_of_interest_flag', 'nullbool')
        cell_line_disease_genotype.allele_carried = valuef('rs_allele_carried')
        cell_line_disease_genotype.cell_line_form = valuef('rs_cell_line_variant_homozygote_heterozygote')
        cell_line_disease_genotype.chormosome = valuef('variant_details_chromosome')
        cell_line_disease_genotype.coordinate = valuef('variant_details_coordinate')
        cell_line_disease_genotype.reference_allele = valuef('variant_details_ref_allele')
        cell_line_disease_genotype.alternative_allele = valuef('variant_details_alt_allele')
        cell_line_disease_genotype.protein_sequence_variants = valuef('description_sequence_changes')

        if valuef('variant_details_assembly'):
            cell_line_disease_genotype.assembly = valuef('variant_details_assembly')
        elif valuef('variant_details_assembly_other'):
            cell_line_disease_genotype.assembly = valuef('variant_details_assembly_other')

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

        dirty = [cell_line_disease_genotype.is_dirty(check_relationship=True)]

        if True in dirty:
            if cell_line_disease_genotype_created:
                logger.info('Added cell line disease associated genotype: %s' % cell_line_disease_genotype)
            else:
                logger.info('Updated cell line disease associated genotype: %s' % cell_line_disease_genotype)

            cell_line_disease_genotype.save()

            return True

        return False


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


# @inject_valuef
# def parse_doc(valuef, source):
#     print valuef('filename_enc')


@inject_valuef
def parse_characterization_pluritest(valuef, source, cell_line):

    # for doc in valuef(['characterisation_pluritest_data', 'uploads']):
    #     parse_doc(doc)

    if valuef('characterisation_pluritest_flag'):
        cell_line_characterization_pluritest, created = CelllineCharacterizationPluritest.objects.get_or_create(cell_line=cell_line)

        cell_line_characterization_pluritest.pluritest_flag = valuef('characterisation_pluritest_flag', 'nullbool')
        cell_line_characterization_pluritest.pluripotency_score = valuef(['characterisation_pluritest_data', 'pluripotency_score'])
        cell_line_characterization_pluritest.novelty_score = valuef(['characterisation_pluritest_data', 'novelty_score'])
        cell_line_characterization_pluritest.microarray_url = valuef(['characterisation_pluritest_data', 'microarray_url'])

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


# @inject_valuef
# def parse_characterization_epipluriscore(valuef, source, cell_line):
#
#     # for doc in valuef(['characterisation_epipluriscore_data', 'uploads']):
#     #     parse_doc(doc)
#
#     if valuef('characterisation_epipluriscore_flag'):
#         cell_line_characterization_epipluriscore, created = CelllineCharacterizationEpipluriscore.objects.get_or_create(cell_line=cell_line)
#
#         cell_line_characterization_epipluriscore.epipluriscore_flag = valuef('characterisation_epipluriscore_flag', 'nullbool')
#         cell_line_characterization_epipluriscore.score = valuef(['characterisation_epipluriscore_data', 'score'])
#

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
