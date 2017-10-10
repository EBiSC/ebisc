from django.conf.urls import patterns, url

urlpatterns = patterns('ebisc.executive.views',

    # Index
    url(r'^$', 'dashboard', name='dashboard'),

    # IDs for registered cell lines
    url(r'^cell-line-ids/$', 'cell_line_ids', name='cell_line_ids'),

    # IDs for created batches
    url(r'^batch-ids/$', 'batch_ids', name='batch_ids'),

    # Cell line
    url(r'^(?P<name>[^/]+)/$', 'cellline', name='cellline'),

    # Cell line batch
    url(r'^(?P<name>[^/]+)/new-batch/$', 'new_batch', name='new_batch'),
    url(r'^(?P<name>[^/]+)/update-batch/(?P<batch_biosample_id>[^/]+)$', 'update_batch', name='update_batch'),
    url(r'^(?P<name>[^/]+)/(?P<batch_biosample_id>[^/]+)/$', 'batch_data', name='batch_data'),
)
