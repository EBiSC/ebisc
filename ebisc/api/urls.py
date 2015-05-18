from tastypie.api import Api

from django.conf.urls import patterns, include, url

from .celllines import CelllineResource

v1_api = Api(api_name='v0')
v1_api.register(CelllineResource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
