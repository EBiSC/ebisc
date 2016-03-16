# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('document', models.FileField(upload_to=b'cms/documents/%Y/%m/%d/', verbose_name='Document')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('path', models.CharField(unique=True, max_length=500, verbose_name='Path')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('body', models.TextField(null=True, verbose_name='Body', blank=True)),
            ],
            options={
                'ordering': ['path'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
