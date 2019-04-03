from django.conf.urls import url
from ebisc.elastic.views import endpoint

urlpatterns = [
    # Search
    url(r'^(?P<path>.+)$', endpoint, name='endpoint'),
]
