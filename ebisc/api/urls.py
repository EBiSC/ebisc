from tastypie.api import Api

from django.conf.urls import patterns, include, url

from .celllines import CelllineResource, CelllineBatchResource

api = Api(api_name='v0')
api.register(CelllineResource())
api.register(CelllineBatchResource())

urlpatterns = patterns('',
    url(r'^', include(api.urls)),
)
