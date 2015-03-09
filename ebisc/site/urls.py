from django.conf.urls import patterns, url

from .views import document

urlpatterns = patterns('',
    url(r'(?P<path>.*)', document, name='document'),
)
