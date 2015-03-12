from tastypie.api import Api

from django.conf.urls import patterns, include, url

from .ecacc import EcaccResource

v1_api = Api(api_name='v1')
v1_api.register(EcaccResource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
