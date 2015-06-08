from tastypie.api import Api

from django.conf.urls import patterns, include, url

from .celllines import CelllineResource

api = Api(api_name='v0')
api.register(CelllineResource())

urlpatterns = patterns('',
    url(r'^', include(api.urls)),
)
