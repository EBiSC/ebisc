from django.conf.urls import url

from . import views

urlpatterns = [
    # Cellline search
    url(r'^$', views.search, name='search'),

    # Pages
    url(r'(?P<path>.*)', views.page, name='page'),
]
