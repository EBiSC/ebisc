from django.db import models

from django.utils.text import slugify


class Page(models.Model):

    published = models.BooleanField(u'Published', default=False)
    updated = models.DateTimeField(u'Last update', auto_now=True)

    path = models.CharField(u'Path', max_length=500, unique=True)
    title = models.CharField(u'Title', max_length=200)
    body = models.TextField(u'Body', null=True, blank=True)

    class Meta:
        verbose_name = u'Page'
        verbose_name_plural = u'Pages'
        ordering = ['path']

    def __unicode__(self):
        return self.title


class Document(models.Model):

    updated = models.DateTimeField(u'Last update', auto_now=True)

    title = models.CharField(u'Title', max_length=200)
    document = models.FileField(u'Document', upload_to='cms/documents/%Y/%m/%d/')

    class Meta:
        verbose_name = u'Document'
        verbose_name_plural = u'Documents'
        ordering = ['title']

    def __unicode__(self):
        return self.title


class FaqCategory(models.Model):

    name = models.CharField(u'Category', max_length=100, unique=True)
    slug = models.SlugField(u'Slug', unique=True)

    class Meta:
        verbose_name = u'FAQ Category'
        verbose_name_plural = u'FAQ Categories'
        ordering = ['slug']

    def __unicode__(self):
        return self.name


class Faq(models.Model):

    published = models.BooleanField(u'Published', default=False)
    updated = models.DateTimeField(u'Last update', auto_now=True)
    position = models.PositiveIntegerField(u'Position', default=0)

    category = models.ForeignKey(FaqCategory, verbose_name=u'Category', related_name='faqs')
    question = models.CharField(u'Question', max_length=1000)
    answer = models.TextField(u'Answer')

    class Meta:
        verbose_name = u'FAQ'
        verbose_name_plural = u'FAQs'
        unique_together = [('question', 'category')]
        ordering = ['position']

    def __unicode__(self):
        return self.question

    @property
    def slug(self):
        return slugify(self.question)
