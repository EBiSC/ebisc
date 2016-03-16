from django.contrib import admin

from .models import Page, Document


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['published', 'path', 'title', 'updated']
    list_display_links = ['title']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document', 'field_markdown', 'updated']
    list_display_links = ['title']

    def field_markdown(self, instance):
        return '[%s](%s)' % (instance.title, instance.document.url)

    field_markdown.short_description = u'Markdown tag'
