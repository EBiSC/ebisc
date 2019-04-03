from django.conf.urls import url
from ebisc.executive.views import dashboard, cell_line_ids, batch_ids, cellline, new_batch, update_batch, batch_data

urlpatterns = [

    # Index
    url(r'^$', dashboard, name='dashboard'),

    # IDs for registered cell lines
    url(r'^cell-line-ids/$', cell_line_ids, name='cell_line_ids'),

    # IDs for created batches
    url(r'^batch-ids/$', batch_ids, name='batch_ids'),

    # Cell line
    url(r'^(?P<name>[^/]+)/$', cellline, name='cellline'),

    # Cell line batch
    url(r'^(?P<name>[^/]+)/new-batch/$', new_batch, name='new_batch'),
    url(r'^(?P<name>[^/]+)/update-batch/(?P<batch_biosample_id>[^/]+)$', update_batch, name='update_batch'),
    url(r'^(?P<name>[^/]+)/(?P<batch_biosample_id>[^/]+)/$', batch_data, name='batch_data'),
]
