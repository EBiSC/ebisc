# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0002_disease_synonyms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinepublication',
            options={'ordering': ('reference_title',), 'verbose_name': 'Cell line publication', 'verbose_name_plural': 'Cell line publications'},
        ),
        migrations.RenameField(
            model_name='celllinepublication',
            old_name='publicationcellline',
            new_name='cellline',
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='reference_id',
            field=models.CharField(max_length=100, null=True, verbose_name='ID', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='reference_title',
            field=models.CharField(default=1, max_length=500, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='reference_type',
            field=models.CharField(default=1, max_length=100, verbose_name='Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='reference_url',
            field=models.URLField(default='', verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='celllinepublication',
            unique_together=set([('cellline', 'reference_url')]),
        ),
        migrations.RemoveField(
            model_name='celllinepublication',
            name='pubmedreference',
        ),
        migrations.RemoveField(
            model_name='celllinepublication',
            name='celllinepublisher',
        ),
        migrations.RemoveField(
            model_name='celllinepublication',
            name='celllinepublicationdoiurl',
        ),
    ]
