import re

from django.http import Http404
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization
from tastypie import fields

from . import IndentedJSONSerializer
from ..celllines.models import Donor, Disease, Cellline, CelllineCultureConditions, CultureMediumOther, CelllineCultureMediumSupplement, CelllineDerivation, CelllineCharacterization, CelllineKaryotype, Organization, CelllineBatch, CelllineBatchImages, BatchCultureConditions, CelllinePublication, CelllineInformationPack


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

    class Meta:
        queryset = CelllineCultureConditions.objects.all()
        include_resource_uri = False
        fields = ('o2_concentration', 'co2_concentration')


# -----------------------------------------------------------------------------
# CelllineCharacterization

class CelllineCharacterizationResource(ModelResource):

    hiv1 = fields.CharField('get_screening_hiv1_display', null=True)
    hiv2 = fields.CharField('get_screening_hiv2_display', null=True)
    hepatitis_b = fields.CharField('get_screening_hepatitis_b_display', null=True)
    hepatitis_c = fields.CharField('get_screening_hepatitis_c_display', null=True)
    mycoplasma = fields.CharField('get_screening_mycoplasma_display', null=True)

    class Meta:
        queryset = CelllineCharacterization.objects.all()
        include_resource_uri = False
        fields = ('hiv1', 'hiv2', 'hepatitis_b', 'hepatitis_c', 'mycoplasma',)


# -----------------------------------------------------------------------------
# CelllineKaryotype

class CelllineKaryotypeResource(ModelResource):

    class Meta:
        queryset = CelllineKaryotype.objects.all()
        include_resource_uri = False
        fields = ('karyotype', 'passage_number')


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

    doid = fields.CharField('icdcode', null=True)
    purl = fields.CharField('purl', null=True)
    name = fields.CharField('disease', null=True)
    synonyms = fields.ListField('synonyms', null=True)

    class Meta:
        queryset = Disease.objects.all()
        include_resource_uri = False
        fields = ('doid', 'name', 'synonyms')

    def dehydrate_synonyms(self, bundle):
        return value_list_of_string(bundle.obj.synonyms)


# -----------------------------------------------------------------------------
# Donor

class DonorResource(ModelResource):

    biosamples_id = fields.CharField('biosamples_id', null=True)
    gender = fields.CharField('gender', null=True)

    class Meta:
        queryset = Donor.objects.all()
        include_resource_uri = False
        fields = ('biosamples_id', 'gender')


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
# Batch

class CelllineBatchResource(ModelResource):

    biosamples_id = fields.CharField('biosamples_id', unique=True)
    batch_id = fields.CharField('batch_id')

    vials_at_roslin = fields.IntegerField('vials_at_roslin', null=True)
    vials_shipped_to_ecacc = fields.IntegerField('vials_shipped_to_ecacc', null=True)
    vials_shipped_to_fraunhoffer = fields.IntegerField('vials_shipped_to_fraunhoffer', null=True)

    culture_conditions = fields.ToOneField(BatchCultureConditionsResource, 'batchcultureconditions', null=True, full=True)

    certificate_of_analysis = fields.DictField(null=True)

    images = fields.ToManyField(CelllineBatchImagesResource, 'images', null=True, full=True)

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

    biosamples_id = fields.CharField('biosamples_id', unique=True)
    ecacc_cat_no = fields.CharField('ecacc_id', unique=True, null=True)

    flag_go_live = fields.BooleanField('available_for_sale', null=True, default=False)
    availability = fields.CharField('get_availability_display')

    name = fields.CharField('name', unique=True)
    alternative_names = fields.CharField('alternative_names', null=True)

    primary_disease_diagnosed = fields.CharField('primary_disease_diagnosis')
    primary_disease = fields.ToOneField(DiseaseResource, 'primary_disease', null=True, full=True)

    primary_cell_type = fields.ToOneField(CelllineDerivationResource, 'derivation', null=True, full=True)
    depositor_cellline_culture_conditions = fields.ToOneField(CelllineCultureConditionsResource, 'celllinecultureconditions', full=True, null=True)
    virology_screening = fields.ToOneField(CelllineCharacterizationResource, 'celllinecharacterization', null=True, full=True)
    cellline_karyotype = fields.ToOneField(CelllineKaryotypeResource, 'karyotype', null=True, full=True)

    donor_age = fields.CharField('donor_age', null=True)
    donor = fields.ToOneField(DonorResource, 'donor', null=True, full=True)

    depositor = fields.ToOneField(OrganizationResource, 'generator', null=True, full=True)

    publications = fields.ToManyField(CelllinePublicationResource, 'publications', null=True, full=True)

    reprogramming_method = fields.DictField(null=True)

    batches = fields.ToManyField(CelllineBatchResource, 'batches', null=True, full=True)

    cell_line_information_packs = fields.ToManyField(CelllineInformationPackResource, 'clips', null=True, full=True)

    class Meta:
        queryset = Cellline.objects.all().select_related(
            'donor__gender',
            'donor_age',
            'integrating_vector__vector',
            'non_integrating_vector__vector',
            'derivation__primary_cell_type',
            'celllinecharacterization',
            'karyotype',
            'generator',
            'primary_disease',
            'celllinecultureconditions__culture_medium_other',
            'integrating_vector__virus',

        ).prefetch_related(
            'clips',
            'batches__batchcultureconditions',
            'batches__images',
            'publications',
            'celllinecultureconditions__medium_supplements__unit',
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

    def dehydrate_reprogramming_method(self, bundle):

        if hasattr(bundle.obj, 'non_integrating_vector'):

            res = {'type': 'Non-integrating vector'}

            if bundle.obj.non_integrating_vector.vector:
                res['data'] = {'vector': bundle.obj.non_integrating_vector.vector}

            return res

        elif hasattr(bundle.obj, 'integrating_vector'):

            res = {'type': 'Integrating vector'}

            if bundle.obj.integrating_vector.vector:
                res['data'] = {
                    'vector': bundle.obj.integrating_vector.vector,
                    'excisable': bundle.obj.integrating_vector.excisable,
                    'absence_reprogramming_vectors': bundle.obj.integrating_vector.absence_reprogramming_vectors,
                }
                if bundle.obj.integrating_vector.virus:
                    res['data']['virus'] = bundle.obj.integrating_vector.virus
                if bundle.obj.integrating_vector.transposon:
                    res['data']['transposon'] = bundle.obj.integrating_vector.transposon

            return res

        else:
            return None

    def dehydrate(self, bundle):
        if not bundle.obj.primary_disease and bundle.obj.primary_disease_diagnosis == '0':
            bundle.data['primary_disease'] = {
                'name': 'normal'
            }
            return bundle
        else:
            return bundle

# -----------------------------------------------------------------------------
# Helpers

def value_list_of_string(string):
    if string is None:
        return []
    else:
        return re.split(r'\s*,\s*', string)

# -----------------------------------------------------------------------------
