import re

from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from . import IndentedJSONSerializer
from ..celllines.models import Donor, Disease, Cellline, Celllinecultureconditions, CellLineKaryotype, Organization


# -----------------------------------------------------------------------------
# CelllineCultureConditions

class CelllineCultureConditionsResource(ModelResource):

    # + culture_medium = models.ForeignKey('CultureMedium', verbose_name=_(u'Culture medium'), blank=True, null=True)
    # + surfacecoating = models.ForeignKey('SurfaceCoating', verbose_name=_(u'Surface coating'), null=True, blank=True)
    # - feedercelltype = models.CharField(_(u'Feeder cell type'), max_length=45, null=True, blank=True)
    # - feedercellid = models.CharField(_(u'Feeder cell id'), max_length=45, null=True, blank=True)
    # + passagemethod = models.ForeignKey('PassageMethod', verbose_name=_(u'Passage method'), blank=True, null=True)
    # - enzymatically = models.ForeignKey('Enzymatically', verbose_name=_(u'Enzymatically'), blank=True, null=True)
    # - enzymefree = models.ForeignKey('EnzymeFree', verbose_name=_(u'Enzyme free'), blank=True, null=True)
    # + o2concentration = models.IntegerField(_(u'O2 concentration'), blank=True, null=True)
    # + co2concentration = models.IntegerField(_(u'Co2 concentration'), blank=True, null=True)

    surface_coating = fields.CharField('surfacecoating', null=True)
    culture_medium = fields.CharField('culture_medium', null=True)
    passage_method = fields.CharField('passagemethod', null=True)

    o2_concentration = fields.IntegerField('o2concentration', null=True)
    co2_concentration = fields.IntegerField('co2concentration', null=True)

    class Meta:
        queryset = Celllinecultureconditions.objects.all()
        include_resource_uri = False
        fields = ('o2_concentration', 'co2_concentration')


# -----------------------------------------------------------------------------
# CellLineKaryotype

class CellLineKaryotypeResource(ModelResource):

    # + karyotype = models.CharField(_(u'Karyotype'), max_length=500, null=True, blank=True)
    # + karyotype_method = models.ForeignKey('KaryotypeMethod', verbose_name=_(u'Karyotype method'), null=True, blank=True)
    # + passage_number = models.IntegerField(_(u'Passage number'), null=True, blank=True)

    karyotype_method = fields.CharField('karyotype_method', null=True)

    class Meta:
        queryset = CellLineKaryotype.objects.all()
        include_resource_uri = False
        fields = ('karyotype', 'passage_number')


# -----------------------------------------------------------------------------
# Disease

class DiseaseResource(ModelResource):

    doid = fields.CharField('icdcode', null=True)
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

    # - biosamplesid = models.CharField(_(u'Biosamples ID'), max_length=12, unique=True)
    # + gender = models.ForeignKey(Gender, verbose_name=_(u'Gender'), blank=True, null=True)
    # - countryoforigin = models.ForeignKey('Country', verbose_name=_(u'Country'), blank=True, null=True)
    # - primarydisease = models.ForeignKey('Disease', verbose_name=_(u'Disease'), blank=True, null=True)
    # - diseaseadditionalinfo = models.CharField(_(u'Disease additional info'), max_length=45, blank=True)
    # - othercelllinefromdonor = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='celllines_othercelllinefromdonor', blank=True, null=True)
    # - parentcellline = models.ForeignKey('Cellline', verbose_name=_(u'Cell line'), related_name='celllines_parentcellline', blank=True, null=True)
    # - providerdonorid = models.CharField(_(u'Provider donor id'), max_length=45, blank=True)
    # - cellabnormalkaryotype = models.CharField(_(u'Cell abnormal karyotype'), max_length=45, blank=True)
    # - donorabnormalkaryotype = models.CharField(_(u'Donor abnormal karyotype'), max_length=45, blank=True)
    # - otherclinicalinformation = models.CharField(_(u'Other clinical information'), max_length=100, blank=True)
    # - phenotype = models.ForeignKey('Phenotype', verbose_name=_(u'Phenotype'), blank=True, null=True)

    gender = fields.CharField('gender', null=True)

    class Meta:
        queryset = Donor.objects.all()
        include_resource_uri = False
        fields = ('gender')


# -----------------------------------------------------------------------------
# Organization

class OrganizationResource(ModelResource):

    # + organizationname = models.CharField(_(u'Organization name'), max_length=100, unique=True, null=True, blank=True)
    # - organizationshortname = models.CharField(_(u'Organization short name'), unique=True, max_length=6, null=True, blank=True)
    # - organizationcontact = models.ForeignKey('Contact', verbose_name=_(u'Contact'), blank=True, null=True)
    # - organizationtype = models.ForeignKey('Orgtype', verbose_name=_(u'Orgtype'), blank=True, null=True)

    name = fields.CharField('organizationname', null=True)

    class Meta:
        queryset = Donor.objects.all()
        include_resource_uri = False
        fields = ('name',)


# -----------------------------------------------------------------------------
# Cellline

class CelllineResource(ModelResource):

    # - celllineaccepted = models.CharField(_(u'Cell line accepted'), max_length=10, choices=ACCEPTED_CHOICES, default='pending')
    # + biosamplesid = models.CharField(_(u'Biosamples ID'), unique=True, max_length=12)
    # + celllinename = models.CharField(_(u'Cell line name'), unique=True, max_length=15)
    # - donor = models.ForeignKey('Donor', verbose_name=_(u'Donor'), blank=True, null=True)
    # - donor_age = models.ForeignKey(AgeRange, verbose_name=_(u'Age'), blank=True, null=True)
    # - generator = models.ForeignKey('Organization', verbose_name=_(u'Generator'), related_name='generator_of_cell_lines')
    # - owner = models.ForeignKey('Organization', verbose_name=_(u'Owner'), null=True, blank=True, related_name='owner_of_cell_lines')
    # - celllineprimarydisease = models.ForeignKey('Disease', verbose_name=_(u'Disease'), blank=True, null=True)
    # - celllinediseaseaddinfo = models.CharField(_(u'Cell line disease info'), max_length=100, null=True, blank=True)
    # - celllinestatus = models.ForeignKey('Celllinestatus', verbose_name=_(u'Cell line status'), blank=True, null=True)
    # + celllinecelltype = models.ForeignKey('Celltype', verbose_name=_(u'Cell type'), blank=True, null=True)
    # - celllinecollection = models.ForeignKey('Celllinecollection', verbose_name=_(u'Cell line collection'), blank=True, null=True)
    # - celllinetissuesource = models.ForeignKey('Tissuesource', verbose_name=_(u'Tissue source'), blank=True, null=True)
    # - celllinetissuetreatment = models.ForeignKey('Clinicaltreatmentb4donation', verbose_name=_(u'Clinical treatment B4 donation'), blank=True, null=True)
    # - celllinetissuedate = models.DateField(_(u'Cell line tissue date'), blank=True, null=True)
    # + celllinenamesynonyms = models.CharField(_(u'Cell line name synonyms'), max_length=500, null=True, blank=True)
    # - depositorscelllineuri = models.CharField(_(u'Depositors cell line URI'), max_length=45, blank=True)
    # - celllinecomments = models.TextField(_(u'Cell line comments'), null=True, blank=True)
    # - celllineecaccurl = models.URLField(_(u'Cell line ECACC URL'), blank=True, null=True)

    biosamples_id = fields.CharField('biosamplesid', unique=True)

    name = fields.CharField('celllinename', unique=True)
    alternate_names = fields.CharField('celllinenamesynonyms')

    cell_type = fields.CharField('celllinecelltype', null=True)
    primary_disease = fields.ToOneField(DiseaseResource, 'celllineprimarydisease', null=True, full=True)
    culture_conditions = fields.ToOneField(CelllineCultureConditionsResource, 'celllinecultureconditions', full=True)
    cellline_karyotype = fields.ToOneField(CellLineKaryotypeResource, 'karyotype', null=True, full=True)

    donor_age = fields.CharField('donor_age', null=True)
    donor = fields.ToOneField(DonorResource, 'donor', full=True)

    depositor = fields.ToOneField(OrganizationResource, 'generator', null=True, full=True)

    reprogramming_method = fields.DictField(null=True)

    class Meta:
        queryset = Cellline.objects.all()
        resource_name = 'cell-lines'

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        detail_uri_name = 'biosamplesid'

        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

        serializer = IndentedJSONSerializer()

        fields = ('biosamples_id', 'name')

    def dehydrate_alternate_names(self, bundle):
        return value_list_of_string(bundle.obj.celllinenamesynonyms)

    def dehydrate_reprogramming_method(self, bundle):

        if hasattr(bundle.obj, 'non_integrating_vector'):

            res = {'type': 'non-integrating vector'}

            if bundle.obj.non_integrating_vector.vector:
                res['data'] = {'vector': bundle.obj.non_integrating_vector.vector}

            return res

        elif hasattr(bundle.obj, 'integrating_vector'):

            res = {'type': 'integrating vector'}

            if bundle.obj.integrating_vector.vector:
                res['data'] = {
                    'vector': bundle.obj.integrating_vector.vector,
                    'excisable': bundle.obj.integrating_vector.excisable,
                }
                if bundle.obj.integrating_vector.virus:
                    res['data']['virus'] = bundle.obj.integrating_vector.virus
                if bundle.obj.integrating_vector.transposon:
                    res['data']['transposon'] = bundle.obj.integrating_vector.transposon

            return res

        else:
            return None


# -----------------------------------------------------------------------------
# Helpers

def value_list_of_string(string):
    if string is None:
        return []
    else:
        return re.split(r'\s*,\s*', string)

# -----------------------------------------------------------------------------
