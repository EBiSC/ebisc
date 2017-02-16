import re

from django.http import Http404
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization
from tastypie import fields

from . import IndentedJSONSerializer
from ..celllines.models import Donor, DonorDisease, DonorDiseaseVariant, Disease, Cellline, CelllineDisease, ModificationVariantDisease, ModificationVariantNonDisease, ModificationIsogenicDisease, ModificationIsogenicNonDisease, ModificationTransgeneExpressionDisease, ModificationTransgeneExpressionNonDisease, ModificationGeneKnockOutDisease, ModificationGeneKnockOutNonDisease, ModificationGeneKnockInDisease, ModificationGeneKnockInNonDisease, CelllineStatus, CelllineCultureConditions, CultureMediumOther, CelllineCultureMediumSupplement, CelllineDerivation, CelllineCharacterization, CelllineCharacterizationPluritest, CelllineKaryotype, Organization, CelllineBatch, CelllineBatchImages, BatchCultureConditions, CelllineAliquot, CelllinePublication, CelllineInformationPack, CelllineDiseaseGenotype, CelllineGeneticModification, GeneticModificationTransgeneExpression, GeneticModificationGeneKnockOut, GeneticModificationGeneKnockIn, GeneticModificationIsogenic


# -----------------------------------------------------------------------------
# CelllineDerivation

class CelllineDerivationResource(ModelResource):

    name = fields.CharField('primary_cell_type', null=True)

    class Meta:
        queryset = CelllineDerivation.objects.all()
        include_resource_uri = False
        fields = ('primary_cell_type',)


# -----------------------------------------------------------------------------
# CelllineCultureConditions

class CultureMediumOtherResource(ModelResource):

    base = fields.CharField('base', null=True)
    protein_source = fields.CharField('protein_source', null=True)
    serum_concentration = fields.IntegerField('serum_concentration', null=True)

    class Meta:
        queryset = CultureMediumOther.objects.all()
        include_resource_uri = False
        fields = ('base', 'protein_source', 'serum_concentration',)


class CelllineCultureMediumSupplementResource(ModelResource):

    supplement = fields.CharField('supplement')
    amount = fields.CharField('amount', null=True)
    unit = fields.CharField('unit', null=True)

    class Meta:
        queryset = CelllineCultureMediumSupplement.objects.all()
        include_resource_uri = False
        fields = ('supplement', 'amount', )


class CelllineCultureConditionsResource(ModelResource):

    surface_coating = fields.CharField('surface_coating', null=True)

    feeder_cell_type = fields.CharField('feeder_cell_type', null=True)
    feeder_cell_id = fields.CharField('feeder_cell_id', null=True)
    passage_method = fields.CharField('passage_method', null=True)
    enzymatically = fields.CharField('enzymatically', null=True)
    enzyme_free = fields.CharField('enzyme_free', null=True)
    o2_concentration = fields.IntegerField('o2_concentration', null=True)
    co2_concentration = fields.IntegerField('co2_concentration', null=True)
    other_culture_environment = fields.CharField('other_culture_environment', null=True)

    culture_medium = fields.CharField('culture_medium', null=True)
    culture_medium_other = fields.ToOneField(CultureMediumOtherResource, 'culture_medium_other', null=True, full=True)

    culture_medium_supplements = fields.ToManyField(CelllineCultureMediumSupplementResource, 'medium_supplements', null=True, full=True)

    passage_number_banked = fields.CharField('passage_number_banked', null=True)
    number_of_vials_banked = fields.CharField('number_of_vials_banked', null=True)
    passage_history = fields.BooleanField('passage_history', null=True)
    culture_history = fields.BooleanField('culture_history', null=True)

    rock_inhibitor_used_at_passage = fields.CharField('get_rock_inhibitor_used_at_passage_display')
    rock_inhibitor_used_at_cryo = fields.CharField('get_rock_inhibitor_used_at_cryo_display')
    rock_inhibitor_used_at_thaw = fields.CharField('get_rock_inhibitor_used_at_thaw_display')

    class Meta:
        queryset = CelllineCultureConditions.objects.all()
        include_resource_uri = False
        fields = ('o2_concentration', 'co2_concentration')


# -----------------------------------------------------------------------------
# CelllineCharacterization

class CelllineCharacterizationVirologyResource(ModelResource):

    virology_screening_flag = fields.BooleanField('virology_screening_flag', null=True)
    hiv1 = fields.CharField('get_screening_hiv1_display', null=True)
    hiv2 = fields.CharField('get_screening_hiv2_display', null=True)
    hepatitis_b = fields.CharField('get_screening_hepatitis_b_display', null=True)
    hepatitis_c = fields.CharField('get_screening_hepatitis_c_display', null=True)
    mycoplasma = fields.CharField('get_screening_mycoplasma_display', null=True)

    class Meta:
        queryset = CelllineCharacterization.objects.all()
        include_resource_uri = False
        fields = ('virology_screening_flag', 'hiv1', 'hiv2', 'hepatitis_b', 'hepatitis_c', 'mycoplasma',)


class CelllineCharacterizationPluritestResource(ModelResource):

    pluritest_flag = fields.BooleanField('pluritest_flag', null=True)
    pluripotency_score = fields.CharField('pluripotency_score', null=True)
    novelty_score = fields.CharField('novelty_score', null=True)

    class Meta:
        queryset = CelllineCharacterizationPluritest.objects.all()
        include_resource_uri = False
        fields = ('pluritest_flag', 'pluripotency_score', 'novelty_score',)


class CelllineCharacterizationCoAResource(ModelResource):

    certificate_of_analysis_flag = fields.BooleanField('certificate_of_analysis_flag', null=True)

    class Meta:
        queryset = CelllineCharacterization.objects.all()
        include_resource_uri = False
        fields = ('certificate_of_analysis_flag')


# -----------------------------------------------------------------------------
# CelllineKaryotype

class CelllineKaryotypeResource(ModelResource):

    class Meta:
        queryset = CelllineKaryotype.objects.all()
        include_resource_uri = False
        fields = ('karyotype', 'karyotype_method', 'passage_number')


# -----------------------------------------------------------------------------
# CelllineGenotyping

class CelllineDiseaseGenotypeResource(ModelResource):

    carries_disease_phenotype_associated_variants_flag = fields.BooleanField('carries_disease_phenotype_associated_variants', null=True)
    variant_of_interest_flag = fields.BooleanField('variant_of_interest', null=True)

    class Meta:
        queryset = CelllineDiseaseGenotype.objects.all()
        include_resource_uri = False
        fields = ('carries_disease_phenotype_associated_variants_flag', 'variant_of_interest_flag')


# -----------------------------------------------------------------------------
# CelllineGenoticModification

class GeneticModificationResource(ModelResource):

    genetic_modification_flag = fields.BooleanField('genetic_modification_flag', null=True)
    types = fields.ListField('types', null=True)

    class Meta:
        queryset = CelllineGeneticModification.objects.all()
        include_resource_uri = False
        fields = ('genetic_modification_flag', 'types')


class GeneticModificationTransgeneExpressionResource(ModelResource):

    delivery_method = fields.CharField('delivery_method', null=True)
    genes = fields.DictField(null=True)

    class Meta:
        queryset = GeneticModificationTransgeneExpression.objects.all()
        include_resource_uri = False
        fields = ('delivery_method', 'genes')

    def dehydrate_genes(self, bundle):
        if hasattr(bundle.obj, 'genes'):
            return [gene.name for gene in bundle.obj.genes.all()]
        else:
            return []


class GeneticModificationGeneKnockOutResource(ModelResource):

    delivery_method = fields.CharField('delivery_method', null=True)
    target_genes = fields.DictField(null=True)

    class Meta:
        queryset = GeneticModificationGeneKnockOut.objects.all()
        include_resource_uri = False
        fields = ('delivery_method', 'target_genes')

    def dehydrate_target_genes(self, bundle):
        if hasattr(bundle.obj, 'target_genes'):
            return [gene.name for gene in bundle.obj.target_genes.all()]
        else:
            return []


class GeneticModificationGeneKnockInResource(ModelResource):

    delivery_method = fields.CharField('delivery_method', null=True)
    target_genes = fields.DictField(null=True)
    transgenes = fields.DictField(null=True)

    class Meta:
        queryset = GeneticModificationGeneKnockIn.objects.all()
        include_resource_uri = False
        fields = ('delivery_method', 'target_genes', 'transgenes')

    def dehydrate_target_genes(self, bundle):
        if hasattr(bundle.obj, 'target_genes'):
            return [gene.name for gene in bundle.obj.target_genes.all()]
        else:
            return []

    def dehydrate_transgenes(self, bundle):
        if hasattr(bundle.obj, 'transgenes'):
            return [gene.name for gene in bundle.obj.transgenes.all()]
        else:
            return []


class GeneticModificationIsogenicResource(ModelResource):

    change_type = fields.CharField('change_type', null=True)
    modified_sequence = fields.CharField('modified_sequence', null=True)
    target_locus = fields.DictField(null=True)

    class Meta:
        queryset = GeneticModificationIsogenic.objects.all()
        include_resource_uri = False
        fields = ('change_type', 'modified_sequence', 'target_locus')

    def dehydrate_target_locus(self, bundle):
        if hasattr(bundle.obj, 'target_locus'):
            return [locus.name for locus in bundle.obj.target_locus.all()]
        else:
            return []


# -----------------------------------------------------------------------------
# Publication

class CelllinePublicationResource(ModelResource):

    pub = fields.CharField('get_reference_type_display')
    pub_id = fields.CharField('reference_id', null=True)
    pub_url = fields.CharField('reference_url')
    pub_title = fields.CharField('reference_title')

    class Meta:
        queryset = CelllinePublication.objects.all()
        include_resource_uri = False
        fields = ('pub', 'pub_id', 'pub_url', 'pub_title')


# -----------------------------------------------------------------------------
# Disease

class DiseaseResource(ModelResource):

    purl = fields.CharField('xpurl', null=True)
    name = fields.CharField('name', null=True)
    synonyms = fields.ListField('synonyms', null=True)

    class Meta:
        queryset = Disease.objects.all()
        include_resource_uri = False
        fields = ('purl', 'name', 'synonyms')

    def dehydrate_synonyms(self, bundle):
        return value_list_of_string(bundle.obj.synonyms)


# -----------------------------------------------------------------------------
# Disease variant/modification resources

class ModificationVariantDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    nucleotide_sequence_hgvs = fields.CharField('nucleotide_sequence_hgvs', null=True)
    protein_sequence_hgvs = fields.CharField('protein_sequence_hgvs', null=True)
    zygosity_status = fields.CharField('zygosity_status', null=True)
    clinvar_id = fields.CharField('clinvar_id', null=True)
    dbsnp_id = fields.CharField('dbsnp_id', null=True)
    dbvar_id = fields.CharField('dbvar_id', null=True)
    publication_pmid = fields.CharField('publication_pmid', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationVariantDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'nucleotide_sequence_hgvs', 'protein_sequence_hgvs', 'zygosity_status', 'clinvar_id', 'dbsnp_id', 'dbvar_id', 'publication_pmid', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        bundle.data.update({
            'type': 'Variant',
            'gene': gene
        })

        return bundle


class ModificationIsogenicDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    nucleotide_sequence_hgvs = fields.CharField('nucleotide_sequence_hgvs', null=True)
    protein_sequence_hgvs = fields.CharField('protein_sequence_hgvs', null=True)
    zygosity_status = fields.CharField('zygosity_status', null=True)
    modification_type = fields.CharField('modification_type', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationIsogenicDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'nucleotide_sequence_hgvs', 'protein_sequence_hgvs', 'zygosity_status', 'modification_type', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        bundle.data.update({
            'type': 'Isogenic modification',
            'gene': gene
        })

        return bundle


class ModificationTransgeneExpressionDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationTransgeneExpressionDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Transgene expression',
            'gene': gene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


class ModificationGeneKnockOutDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationGeneKnockOutDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Gene knock-out',
            'gene': gene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


class ModificationGeneKnockInDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    chromosome_location_transgene = fields.CharField('chromosome_location_transgene', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationGeneKnockInDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'chromosome_location_transgene', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.target_gene:
            target_gene = bundle.obj.target_gene.name
        else:
            target_gene = None

        if bundle.obj.transgene:
            transgene = bundle.obj.transgene.name
        else:
            transgene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Gene knock-in',
            'target_gene': target_gene,
            'transgene': transgene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


# -----------------------------------------------------------------------------
# Cell line Disease

class CelllineDiseaseResource(ModelResource):

    primary_disease = fields.BooleanField('primary_disease', null=True, default=False)

    free_text_name = fields.CharField('disease_not_normalised', null=True)
    notes = fields.CharField('notes', null=True)

    disease_stage = fields.CharField('disease_stage', null=True)
    affected_status = fields.CharField('affected_status', null=True)
    carrier = fields.CharField('carrier', null=True)

    # Variants
    modification_variants = fields.ToManyField(ModificationVariantDiseaseResource, 'genetic_modification_cellline_disease_variants', null=True, full=True)

    # Transgene
    transgene_expression = fields.ToManyField(ModificationTransgeneExpressionDiseaseResource, 'genetic_modification_cellline_disease_transgene_expression', null=True, full=True)

    # Isogenic
    isogenic_modifications = fields.ToManyField(ModificationVariantDiseaseResource, 'genetic_modification_cellline_disease_isogenic', null=True, full=True)

    # Gene knock-out
    gene_knock_out = fields.ToManyField(ModificationGeneKnockOutDiseaseResource, 'genetic_modification_cellline_disease_gene_knock_out', null=True, full=True)

    # Gene knock-in
    gene_knock_in = fields.ToManyField(ModificationGeneKnockInDiseaseResource, 'genetic_modification_cellline_disease_gene_knock_in', null=True, full=True)

    class Meta:
        queryset = CelllineDisease.objects.all()
        include_resource_uri = False
        fields = ('other', 'free_text', 'primary_disease', 'disease_stage', 'affected_status', 'carrier')

    def dehydrate(self, bundle):

        if bundle.obj.disease:
            bundle.data.update({
                'name': bundle.obj.disease.name,
                'purl': bundle.obj.disease.xpurl,
                'synonyms': value_list_of_string(bundle.obj.disease.synonyms),
            })

        # Combine all disease variants in one field 'variants'
        variants = []

        if hasattr(bundle.obj, 'genetic_modification_cellline_disease_variants'):
            variants.extend(bundle.data['modification_variants'])
        if hasattr(bundle.obj, 'genetic_modification_cellline_disease_transgene_expression'):
            variants.extend(bundle.data['transgene_expression'])
        if hasattr(bundle.obj, 'genetic_modification_cellline_disease_isogenic'):
            variants.extend(bundle.data['isogenic_modifications'])
        if hasattr(bundle.obj, 'genetic_modification_cellline_disease_gene_knock_out'):
            variants.extend(bundle.data['gene_knock_out'])
        if hasattr(bundle.obj, 'genetic_modification_cellline_disease_gene_knock_in'):
            variants.extend(bundle.data['gene_knock_in'])

        bundle.data.update({
            'variants': variants,
        })

        # Delete all disease variants fields that are combined in one field 'variants'
        delete_fields = ['modification_variants', 'transgene_expression', 'isogenic_modifications', 'gene_knock_out', 'gene_knock_in']

        for field in delete_fields:
            del bundle.data[field]

        return bundle


# -----------------------------------------------------------------------------
# Donor Disease Variant resource

class DonorDiseaseVariantResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    nucleotide_sequence_hgvs = fields.CharField('nucleotide_sequence_hgvs', null=True)
    protein_sequence_hgvs = fields.CharField('protein_sequence_hgvs', null=True)
    zygosity_status = fields.CharField('zygosity_status', null=True)
    clinvar_id = fields.CharField('clinvar_id', null=True)
    dbsnp_id = fields.CharField('dbsnp_id', null=True)
    dbvar_id = fields.CharField('dbvar_id', null=True)
    publication_pmid = fields.CharField('publication_pmid', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = DonorDiseaseVariant.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'nucleotide_sequence_hgvs', 'protein_sequence_hgvs', 'zygosity_status', 'clinvar_id', 'dbsnp_id', 'dbvar_id', 'publication_pmid', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        bundle.data.update({
            'gene': gene,
        })

        return bundle


# -----------------------------------------------------------------------------
# Donor Disease

class DonorDiseaseResource(ModelResource):

    primary_disease = fields.BooleanField('primary_disease', null=True, default=False)

    free_text_name = fields.CharField('disease_not_normalised', null=True)
    notes = fields.CharField('notes', null=True)

    disease_stage = fields.CharField('disease_stage', null=True)
    affected_status = fields.CharField('affected_status', null=True)
    carrier = fields.CharField('carrier', null=True)

    # Variants
    variants = fields.ToManyField(DonorDiseaseVariantResource, 'donor_disease_variants', null=True, full=True)

    class Meta:
        queryset = DonorDisease.objects.all().select_related(
            'donor_disease_variants',
        ).prefetch_related(
            'donor_disease_variants__gene',
        )
        include_resource_uri = False
        fields = ('other', 'free_text', 'primary_disease', 'disease_stage', 'affected_status', 'carrier')

    def dehydrate(self, bundle):

        if bundle.obj.disease:
            bundle.data.update({
                'name': bundle.obj.disease.name,
                'purl': bundle.obj.disease.xpurl,
                'synonyms': value_list_of_string(bundle.obj.disease.synonyms)
            })

        return bundle


# -----------------------------------------------------------------------------
# Donor

class DonorResource(ModelResource):

    biosamples_id = fields.CharField('biosamples_id', null=True)
    gender = fields.CharField('gender', null=True)
    internal_donor_ids = fields.ListField('provider_donor_ids', null=True)
    country_of_origin = fields.CharField('country_of_origin', null=True)
    ethnicity = fields.CharField('ethnicity', null=True)
    karyotype = fields.CharField('karyotype', null=True)

    # Diseases
    diseases = fields.ToManyField(DonorDiseaseResource, 'diseases', null=True, full=True)

    class Meta:
        queryset = Donor.objects.all().select_related(
            'gender',
            'diseases',
        ).prefetch_related(
            'diseases__disease',
        )

        include_resource_uri = False
        fields = ('biosamples_id', 'gender', 'internal_donor_ids', 'country_of_origin', 'ethnicity', 'karyotype')


# -----------------------------------------------------------------------------
# Genetic modification Non-Disease resources

class ModificationVariantNonDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    nucleotide_sequence_hgvs = fields.CharField('nucleotide_sequence_hgvs', null=True)
    protein_sequence_hgvs = fields.CharField('protein_sequence_hgvs', null=True)
    zygosity_status = fields.CharField('zygosity_status', null=True)
    clinvar_id = fields.CharField('clinvar_id', null=True)
    dbsnp_id = fields.CharField('dbsnp_id', null=True)
    dbvar_id = fields.CharField('dbvar_id', null=True)
    publication_pmid = fields.CharField('publication_pmid', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationVariantNonDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'nucleotide_sequence_hgvs', 'protein_sequence_hgvs', 'zygosity_status', 'clinvar_id', 'dbsnp_id', 'dbvar_id', 'publication_pmid', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        bundle.data.update({
            'type': 'Variant',
            'gene': gene
        })

        return bundle


class ModificationIsogenicNonDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    nucleotide_sequence_hgvs = fields.CharField('nucleotide_sequence_hgvs', null=True)
    protein_sequence_hgvs = fields.CharField('protein_sequence_hgvs', null=True)
    zygosity_status = fields.CharField('zygosity_status', null=True)
    modification_type = fields.CharField('modification_type', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationIsogenicNonDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'nucleotide_sequence_hgvs', 'protein_sequence_hgvs', 'zygosity_status', 'modification_type', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        bundle.data.update({
            'type': 'Isogenic modification',
            'gene': gene
        })

        return bundle


class ModificationTransgeneExpressionNonDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationTransgeneExpressionNonDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Transgene expression',
            'gene': gene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


class ModificationGeneKnockOutNonDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationGeneKnockOutNonDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.gene:
            gene = bundle.obj.gene.name
        else:
            gene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Gene knock-out',
            'gene': gene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


class ModificationGeneKnockInNonDiseaseResource(ModelResource):

    chromosome_location = fields.CharField('chromosome_location', null=True)
    chromosome_location_transgene = fields.CharField('chromosome_location_transgene', null=True)
    delivery_method = fields.CharField('delivery_method', null=True)
    notes = fields.CharField('notes', null=True)

    class Meta:
        queryset = ModificationGeneKnockInNonDisease.objects.all()
        include_resource_uri = False
        fields = ('chromosome_location', 'chromosome_location_transgene', 'delivery_method', 'notes')

    def dehydrate(self, bundle):

        if bundle.obj.target_gene:
            target_gene = bundle.obj.target_gene.name
        else:
            target_gene = None

        if bundle.obj.transgene:
            transgene = bundle.obj.transgene.name
        else:
            transgene = None

        if bundle.obj.virus:
            virus = bundle.obj.virus.name
        else:
            virus = None

        if bundle.obj.transposon:
            transposon = bundle.obj.transposon.name
        else:
            transposon = None

        bundle.data.update({
            'type': 'Gene knock-in',
            'target_gene': target_gene,
            'transgene': transgene,
            'virus': virus,
            'transposon': transposon,
        })

        return bundle


# -----------------------------------------------------------------------------
# Organization

class OrganizationResource(ModelResource):

    name = fields.CharField('name', null=True)

    class Meta:
        queryset = Organization.objects.all()
        include_resource_uri = False
        fields = ('name',)


# -----------------------------------------------------------------------------
# Batch Images

class CelllineBatchImagesResource(ModelResource):
    image_file = fields.FileField('image')
    image_md5 = fields.CharField('md5')
    magnification = fields.CharField('magnification', null=True)
    time_point = fields.CharField('time_point', null=True)

    class Meta:
        queryset = CelllineBatchImages.objects.all()
        include_resource_uri = False
        fields = ('image_file', 'image_md5', 'magnification', 'time_point')


# -----------------------------------------------------------------------------
# Batch Culture conditions

class BatchCultureConditionsResource(ModelResource):
    culture_medium = fields.CharField('culture_medium', null=True)
    passage_method = fields.CharField('passage_method', null=True)
    matrix = fields.CharField('matrix', null=True)
    o2_concentration = fields.CharField('o2_concentration', null=True)
    co2_concentration = fields.CharField('co2_concentration', null=True)
    temperature = fields.CharField('temperature', null=True)

    class Meta:
        queryset = BatchCultureConditions.objects.all()
        include_resource_uri = False
        fields = ('culture_medium')


# -----------------------------------------------------------------------------
# Batch Vials

class CelllineAliquotResource(ModelResource):
    biosamples_id = fields.CharField('biosamples_id')
    name = fields.CharField('name')
    number = fields.CharField('number')

    class Meta:
        queryset = CelllineAliquot.objects.all()
        include_resource_uri = False
        fields = ('biosamples_id', 'name')


# -----------------------------------------------------------------------------
# Batch

class CelllineBatchResource(ModelResource):

    biosamples_id = fields.CharField('biosamples_id', unique=True)
    batch_id = fields.CharField('batch_id')

    batch_type = fields.CharField('get_batch_type_display')

    vials_at_roslin = fields.IntegerField('vials_at_roslin', null=True)
    vials_shipped_to_ecacc = fields.IntegerField('vials_shipped_to_ecacc', null=True)
    vials_shipped_to_fraunhoffer = fields.IntegerField('vials_shipped_to_fraunhoffer', null=True)

    culture_conditions = fields.ToOneField(BatchCultureConditionsResource, 'batchcultureconditions', null=True, full=True)

    certificate_of_analysis = fields.DictField(null=True)

    images = fields.ToManyField(CelllineBatchImagesResource, 'images', null=True, full=True)

    vials = fields.ToManyField(CelllineAliquotResource, 'aliquots', null=True, full=True)

    class Meta:
        queryset = CelllineBatch.objects.all()
        resource_name = 'batches'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        detail_uri_name = 'biosamples_id'

        authentication = ApiKeyAuthentication()
        authorization = ReadOnlyAuthorization()

        serializer = IndentedJSONSerializer()

        fields = ('biosamples_id', 'batch_id')

    def get_schema(self, request, **kwargs):
        raise Http404

    def dehydrate_certificate_of_analysis(self, bundle):

        if not bundle.obj.certificate_of_analysis:
            return None
        else:
            return {
                'file': bundle.obj.certificate_of_analysis.url,
                'md5': bundle.obj.certificate_of_analysis_md5,
            }


# -----------------------------------------------------------------------------
# Cell line status log

class CelllineStatusResource(ModelResource):

    status = fields.CharField('get_status_display')

    class Meta:
        queryset = CelllineStatus.objects.all()
        include_resource_uri = False
        fields = ('status', 'comment', 'updated')


# -----------------------------------------------------------------------------
# Cell line information packs (CLIPS)

class CelllineInformationPackResource(ModelResource):

    clip_file = fields.FileField('clip_file')
    md5 = fields.CharField('md5')
    version = fields.CharField('version', null=True)

    class Meta:
        queryset = CelllineInformationPack.objects.all()
        include_resource_uri = False
        fields = ('clip_file', 'md5', 'version', 'updated')


# -----------------------------------------------------------------------------
# Cellline

class CelllineResource(ModelResource):

    # IDs
    biosamples_id = fields.CharField('biosamples_id', unique=True)
    ecacc_cat_no = fields.CharField('ecacc_id', unique=True, null=True)

    # Names
    name = fields.CharField('name', unique=True)
    alternative_names = fields.CharField('alternative_names', null=True)

    # Validation
    validation_status = fields.CharField('get_validated_display')

    # Availability
    availability = fields.CharField('current_status__get_status_display', null=True)

    # ECACC flag for importing lines
    flag_go_live = fields.BooleanField('available_for_sale', null=True, default=False)

    # Status
    status_log = fields.ToManyField(CelllineStatusResource, 'statuses', null=True, full=True)

    # Disease
    primary_disease_diagnosed = fields.CharField('has_diseases', null=True)
    primary_disease = fields.DictField(null=True)
    disease_names = fields.ListField('all_diseases', null=True)
    disease_associated_phenotypes = fields.ListField('disease_associated_phenotypes', null=True)
    non_disease_associated_phenotypes = fields.ListField('non_disease_associated_phenotypes', null=True)

    # Cell line diseases for genetical modified lines
    diseases = fields.ToManyField(CelllineDiseaseResource, 'diseases', null=True, full=True)

    # Donor
    donor_age = fields.CharField('donor_age', null=True)
    donor = fields.ToOneField(DonorResource, 'donor', null=True, full=True)

    # Depositor
    depositor = fields.ToOneField(OrganizationResource, 'generator', null=True, full=True)

    # Derivation
    primary_cell_type = fields.ToOneField(CelllineDerivationResource, 'derivation', null=True, full=True)
    reprogramming_method = fields.DictField(null=True)
    reprogramming_method_vector_free_types = fields.DictField(null=True)

    # Culture conditions
    depositor_cellline_culture_conditions = fields.ToOneField(CelllineCultureConditionsResource, 'celllinecultureconditions', full=True, null=True)

    # Characterization
    virology_screening = fields.ToOneField(CelllineCharacterizationVirologyResource, 'celllinecharacterization', null=True, full=True)
    cellline_certificate_of_analysis = fields.ToOneField(CelllineCharacterizationCoAResource, 'celllinecharacterization', null=True, full=True)
    characterization_pluritest = fields.ToOneField(CelllineCharacterizationPluritestResource, 'celllinecharacterizationpluritest', null=True, full=True)

    # Genotyping
    cellline_karyotype = fields.ToOneField(CelllineKaryotypeResource, 'karyotype', null=True, full=True)
    cellline_disease_associated_genotype = fields.ToOneField(CelllineDiseaseGenotypeResource, 'genotyping_variant', null=True, full=True)

    # Genetic modifications (Old fields)
    genetic_modification = fields.ToOneField(GeneticModificationResource, 'genetic_modification', null=True, full=True)
    genetic_modification_gene_knock_out = fields.ToOneField(GeneticModificationGeneKnockOutResource, 'genetic_modification_gene_knock_out', null=True, full=True)
    genetic_modification_gene_knock_in = fields.ToOneField(GeneticModificationGeneKnockInResource, 'genetic_modification_gene_knock_in', null=True, full=True)
    genetic_modification_transgene_expression = fields.ToOneField(GeneticModificationTransgeneExpressionResource, 'genetic_modification_transgene_expression', null=True, full=True)
    genetic_modification_isogenic = fields.ToOneField(GeneticModificationIsogenicResource, 'genetic_modification_isogenic', null=True, full=True)

    # Genetic modifications (New fields)
    gen_mod_modification_variants = fields.ToManyField(ModificationVariantNonDiseaseResource, 'genetic_modification_cellline_variants', null=True, full=True)

    gen_mod_transgene_expression = fields.ToManyField(ModificationTransgeneExpressionNonDiseaseResource, 'genetic_modification_cellline_transgene_expression', null=True, full=True)

    gen_mod_isogenic_modifications = fields.ToManyField(ModificationIsogenicNonDiseaseResource, 'genetic_modification_cellline_isogenic', null=True, full=True)

    gen_mod_gene_knock_out = fields.ToManyField(ModificationGeneKnockOutNonDiseaseResource, 'genetic_modification_cellline_gene_knock_out', null=True, full=True)

    gen_mod_gene_knock_in = fields.ToManyField(ModificationGeneKnockInNonDiseaseResource, 'genetic_modification_cellline_gene_knock_in', null=True, full=True)

    # Documents
    cell_line_information_packs = fields.ToManyField(CelllineInformationPackResource, 'clips', null=True, full=True)
    publications = fields.ToManyField(CelllinePublicationResource, 'publications', null=True, full=True)

    # Batches
    batches = fields.ToManyField(CelllineBatchResource, 'batches', null=True, full=True)

    class Meta:
        queryset = Cellline.objects.all().select_related(
            'donor__gender',
            'donor_age',
            'integrating_vector__vector',
            'non_integrating_vector__vector',
            'derivation__primary_cell_type',
            'celllinecharacterization',
            'karyotype',
            'genotyping_variant',
            'generator',
            'celllinecultureconditions__culture_medium_other',
            'integrating_vector__virus',
            'vector_free_reprogramming_factors',

        ).prefetch_related(
            'diseases',
            'donor__diseases',
            'clips',
            'batches__batchcultureconditions',
            'batches__images',
            'publications',
            'celllinecultureconditions__medium_supplements__unit',
            'genetic_modification_cellline_variants',
            'genetic_modification_cellline_transgene_expression',
            'genetic_modification_cellline_isogenic',
            'genetic_modification_cellline_gene_knock_out',
            'genetic_modification_cellline_gene_knock_in',
        )

        resource_name = 'cell-lines'

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        detail_uri_name = 'biosamples_id'

        authentication = ApiKeyAuthentication()
        authorization = ReadOnlyAuthorization()

        serializer = IndentedJSONSerializer()

        fields = ('biosamples_id', 'name')

    def get_schema(self, request, **kwargs):
        raise Http404

    def dehydrate_alternative_names(self, bundle):
        return value_list_of_string(bundle.obj.alternative_names)

    def dehydrate_flag_go_live(self, bundle):
        if bundle.obj.available_for_sale is not None:
            # Withdrawn lines also get imported by ECACC
            if bundle.obj.current_status.status == 'withdrawn':
                return True
            else:
                return bundle.obj.available_for_sale
        else:
            return False

    def dehydrate_reprogramming_method_vector_free_types(self, bundle):
        if hasattr(bundle.obj, 'vector_free_reprogramming_factors'):
            if bundle.obj.vector_free_reprogramming_factors.factors:
                factors = [factor.name for factor in bundle.obj.vector_free_reprogramming_factors.factors.all()]
                return factors
        else:
            return []

    def dehydrate_reprogramming_method(self, bundle):

        if hasattr(bundle.obj, 'non_integrating_vector'):

            data = {}

            if bundle.obj.non_integrating_vector.vector:
                data['vector'] = bundle.obj.non_integrating_vector.vector
                if bundle.obj.non_integrating_vector.genes:
                    genes = [gene.name for gene in bundle.obj.non_integrating_vector.genes.all()]
                    data['non_integrating_vector_gene_list'] = genes

            if bundle.obj.non_integrating_vector.detectable:
                data.update({
                    'non_integrating_vector_detectable': bundle.obj.non_integrating_vector.detectable,
                    'non_integrating_vector_detection_notes': bundle.obj.non_integrating_vector.detectable_notes,
                    'non_integrating_vector_methods': bundle.obj.non_integrating_vector.methods,
                })

            return {
                'type': 'Non-integrating vector',
                'data': data
            }

        elif hasattr(bundle.obj, 'integrating_vector'):

            data = {}

            if bundle.obj.integrating_vector.vector:
                data.update({
                    'vector': bundle.obj.integrating_vector.vector,
                    'excisable': bundle.obj.integrating_vector.excisable,
                    'absence_reprogramming_vectors': bundle.obj.integrating_vector.absence_reprogramming_vectors,
                })
                if bundle.obj.integrating_vector.virus:
                    data['virus'] = bundle.obj.integrating_vector.virus
                if bundle.obj.integrating_vector.transposon:
                    data['transposon'] = bundle.obj.integrating_vector.transposon
                if bundle.obj.integrating_vector.genes:
                    genes = [gene.name for gene in bundle.obj.integrating_vector.genes.all()]
                    data['integrating_vector_gene_list'] = genes

            if bundle.obj.integrating_vector.silenced:
                data.update({
                    'integrating_vector_silenced': bundle.obj.integrating_vector.silenced,
                    'integrating_vector_silencing_notes': bundle.obj.integrating_vector.silenced_notes,
                    'integrating_vector_methods': bundle.obj.integrating_vector.methods,
                })

            return {
                'type': 'Integrating vector',
                'data': data,
            }

        else:
            return None

    def dehydrate_primary_disease(self, bundle):
        if bundle.obj.primary_disease is not None:
            if bundle.obj.primary_disease.disease:
                synonyms = [s.strip() for s in bundle.obj.primary_disease.disease.synonyms.split(',')]
                if bundle.obj.primary_disease.disease.name == 'normal':
                    name = 'Normal'
                else:
                    name = bundle.obj.primary_disease.disease.name
                return {
                    'purl': bundle.obj.primary_disease.disease.xpurl,
                    'name': name,
                    'synonyms': synonyms,
                }
            elif bundle.obj.primary_disease.disease_not_normalised:
                return {
                    'name': bundle.obj.primary_disease.disease_not_normalised,
                }
            elif bundle.obj.primary_disease.notes:
                return {
                    'name': bundle.obj.primary_disease.notes,
                }
            else:
                return None
        else:
            return None

    def dehydrate_primary_disease_diagnosed(self, bundle):
        if bundle.obj.has_diseases is True:
            return "1"
        else:
            return "0"

    def dehydrate(self, bundle):

        # Combine all non-disease related modifications in one field: 'genetic_modifications_non_disease'
        modifications = []

        if hasattr(bundle.obj, 'genetic_modification_cellline_variants'):
            if bundle.obj.genetic_modification_cellline_variants.all():
                modifications.extend(bundle.data['gen_mod_modification_variants'])

        if hasattr(bundle.obj, 'genetic_modification_cellline_transgene_expression'):
            if bundle.obj.genetic_modification_cellline_transgene_expression.all():
                modifications.extend(bundle.data['gen_mod_transgene_expression'])

        if hasattr(bundle.obj, 'genetic_modification_cellline_isogenic'):
            if bundle.obj.genetic_modification_cellline_isogenic.all():
                modifications.extend(bundle.data['gen_mod_isogenic_modifications'])

        if hasattr(bundle.obj, 'genetic_modification_cellline_gene_knock_out'):
            if bundle.obj.genetic_modification_cellline_gene_knock_out.all():
                modifications.extend(bundle.data['gen_mod_gene_knock_out'])

        if hasattr(bundle.obj, 'genetic_modification_cellline_gene_knock_in'):
            if bundle.obj.genetic_modification_cellline_gene_knock_in.all():
                modifications.extend(bundle.data['gen_mod_gene_knock_in'])

        bundle.data.update({
            'genetic_modifications_non_disease': modifications,
        })

        # Delete extra fields that are now combined in 'genetic_modifications_non_disease'
        delete_fields = ['gen_mod_modification_variants', 'gen_mod_transgene_expression', 'gen_mod_isogenic_modifications', 'gen_mod_gene_knock_out', 'gen_mod_gene_knock_in']

        for field in delete_fields:
            del bundle.data[field]

        return bundle


# -----------------------------------------------------------------------------
# Helpers

def value_list_of_string(string):
    if string is None:
        return []
    else:
        return re.split(r'\s*,\s*', string)

# -----------------------------------------------------------------------------
