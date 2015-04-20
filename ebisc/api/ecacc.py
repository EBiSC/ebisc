from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from . import IndentedJSONSerializer
from ..celllines.models import Cellline, Celltype, Tissuesource, CellLineKaryotype


class CelltypeResource(ModelResource):

    class Meta:
        queryset = Celltype.objects.all()
        include_resource_uri = False


class TissuesourceResource(ModelResource):

    class Meta:
        queryset = Tissuesource.objects.all()
        include_resource_uri = False


class EcaccResource(ModelResource):

    ecacc_catalogue_number = fields.CharField(unique=True)
    description = fields.CharField()
    celltype = fields.ToOneField(CelltypeResource, 'celllinecelltype', full=True)
    tissuesource = fields.ToOneField(TissuesourceResource, 'celllinetissuesource', full=True)
    reprogrammingmethod1 = fields.CharField()
    reprogrammingmethod2 = fields.CharField()
    reprogrammingmethod3 = fields.CharField()
    culturemedium = fields.CharField()
    passagemethod = fields.CharField()
    karyotype = fields.ToOneField(CellLineKaryotype, 'celllinekaryotype', full=True)
    donor_phenotype = fields.CharField()

    class Meta:
        queryset = Cellline.objects.all()
        resource_name = 'ecacc'

        serializer = IndentedJSONSerializer()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

        excludes = ('id', 'biosamplesid', 'celllinecomments', 'celllinediseaseaddinfo', 'celllineecaccurl', 'celllinenamesynonyms', 'celllinetissuedate', 'celllineupdate', 'depositorscelllineuri')

    def dehydrate(self, bundle):

        if hasattr(bundle.obj, 'celllinelab'):
            bundle.data['reprogrammingmethod1'] = bundle.obj.celllinelab.reprogrammingmethod1
            bundle.data['reprogrammingmethod2'] = bundle.obj.celllinelab.reprogrammingmethod2
            bundle.data['reprogrammingmethod3'] = bundle.obj.celllinelab.reprogrammingmethod3

        if hasattr(bundle.obj, 'celllinecultureconditions'):
            bundle.data['culturemedium'] = bundle.obj.celllinecultureconditions.culturemedium
            bundle.data['passagemethod'] = bundle.obj.celllinecultureconditions.passagemethod

        bundle.data['donor_phenotype'] = bundle.obj.celllinedonor.phenotype

        return bundle
