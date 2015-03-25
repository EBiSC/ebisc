from django.conf.urls import patterns, url

urlpatterns = patterns('ebisc.search.views',
    # Search - layout
    url(r'^$', 'search', name='search'),

    # Search - develop
    url(r'^develop/$', 'search_develop'),

    # Cell line
    url(r'^(?P<biosamples_id>[^/]+)/$', 'cellline', name='cellline'),
)
