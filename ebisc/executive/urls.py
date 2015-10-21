from django.conf.urls import patterns, url

urlpatterns = patterns('ebisc.executive.views',
    # Index
    url(r'^$', 'dashboard', name='dashboard'),

    # Cell line
    url(r'^(?P<biosamples_id>[^/]+)/$', 'cellline', name='cellline'),
    url(r'^(?P<biosamples_id>[^/]+)/accept/$', 'accept', name='accept'),
    url(r'^(?P<biosamples_id>[^/]+)/(?P<batch_biosample_id>[^/]+)/$', 'batch_data', name='batch_data'),
)
