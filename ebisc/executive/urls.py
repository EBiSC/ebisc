from django.conf.urls import patterns, url

urlpatterns = patterns('ebisc.executive.views',
    # Index
    url(r'^$', 'dashboard', name='dashboard'),

    # Cell line
    url(r'^(?P<name>[^/]+)/$', 'cellline', name='cellline'),
    url(r'^(?P<name>[^/]+)/accept/$', 'accept', name='accept'),
    url(r'^(?P<name>[^/]+)/availability/$', 'availability', name='availability'),
    url(r'^(?P<name>[^/]+)/(?P<batch_biosample_id>[^/]+)/$', 'batch_data', name='batch_data'),
)
