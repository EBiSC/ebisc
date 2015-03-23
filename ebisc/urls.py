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

    # CMS
    url(r'^cms/', include('cms.urls')),

    # API
    url(r'^api/', include('ebisc.api.urls')),

    # Executive dashboard
    url(r'^exec-dash/', include('ebisc.executive.urls', namespace='executive')),

    # Cell line search
    url(r'^search/', include('ebisc.search.urls', namespace='search')),

    # Site
    url(r'', include('ebisc.site.urls', namespace='site')),
)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

'''
/login/
/logout/

/search/
/search/id/

/depositor/
/depositor/id/
'''
