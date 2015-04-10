from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.utils.translation import ugettext as _

admin.site.site_header = _(u'EBiSC Administration')
admin.site.site_title = _(u'EBiSC Administration')
admin.site.index_title = ''

urlpatterns = patterns('',
    # Admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    # Elastic proxy
    url(r'^es/', include('ebisc.elastic.urls', namespace='elastic')),

    # API
    url(r'^api/', include('ebisc.api.urls')),

    # Executive dashboard
    url(r'^executive/', include('ebisc.executive.urls', namespace='executive')),

    # Cell line search
    url(r'', include('ebisc.search.urls', namespace='search')),

    # Site
    # url(r'', include('ebisc.site.urls', namespace='site')),
)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
