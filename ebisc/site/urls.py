from django.conf.urls import url

from . import views

urlpatterns = [
    # Cellline search
    url(r'^$', views.search, name='search'),

    # FAQ
    url(r'^faq/(?P<category>([^/]+))/$', views.faq, name='faq'),

    # Pages
    url(r'(?P<path>.*)', views.page, name='page'),
]
