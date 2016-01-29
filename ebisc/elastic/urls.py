from django.conf.urls import url

urlpatterns = [
    # Search
    url(r'^(?P<path>.+)$', 'ebisc.elastic.views.endpoint', name='endpoint'),
]
