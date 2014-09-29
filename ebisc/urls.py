from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_header = u'EBiSC administration'
admin.site.index_title = u'EBiSC administration'
