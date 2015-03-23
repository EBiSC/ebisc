from django.conf.urls import patterns, url

urlpatterns = patterns('ebisc.search.views',
    # Search
    url(r'^$', 'search', name='search'),

    # Cell line
    url(r'^(?P<biosamples_id>[^/]+)/$', 'cellline', name='cellline'),
)
