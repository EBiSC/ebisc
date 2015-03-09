from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # CMS
    url(r'^cms/', include('cms.urls')),

    # Site
    url(r'', include('ebisc.site.urls', namespace='site')),
)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
