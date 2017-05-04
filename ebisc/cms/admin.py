from django.contrib import admin

from .models import Page, Document, Faq, FaqCategory


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


@admin.register(FaqCategory)
class FaqCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['position', 'published', 'question', 'category', 'updated']
    list_display_links = ['question']
    list_filter = ['category__name']
    list_editable = ['position']
