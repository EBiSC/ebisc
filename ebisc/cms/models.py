from django.db import models


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
