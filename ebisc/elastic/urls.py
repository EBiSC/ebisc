from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Index
    url(r'^(?P<path>.+)$', 'ebisc.elastic.views.endpoint', name='endpoint'),
)
