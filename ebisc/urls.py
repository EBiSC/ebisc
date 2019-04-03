from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.utils.translation import ugettext as _

admin.site.site_header = _(u'EBiSC Administration')
admin.site.site_title = _(u'EBiSC Administration')
admin.site.index_title = ''

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'^login/$', login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    # Elastic proxy
    url(r'^es/', include('ebisc.elastic.urls', namespace='elastic')),

    # API
    url(r'^api/', include('ebisc.api.urls')),

    # Executive dashboard
    url(r'^executive/', include('ebisc.executive.urls', namespace='executive')),

    # Site
    url(r'', include('ebisc.site.urls', namespace='site')),
]

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
