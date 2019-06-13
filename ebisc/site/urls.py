from django.conf.urls import url

from . import views

urlpatterns = [
    # Cellline search
    url(r'^$', views.search, name='search'),

    # FAQ
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^faq/(?P<category>([^/]+))/$', views.faq_category, name='faq category'),

    # Pages
    url(r'(?P<path>.*)', views.page, name='page'),
]
