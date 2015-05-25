# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0007_auto_20150525_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='catalog',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gene ID source', choices=[(b'entrez', 'Entrez'), (b'ensembl', 'Ensembl')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gene',
            name='catalog_id',
            field=models.CharField(max_length=20, null=True, verbose_name='ID', blank=True),
            preserve_default=True,
        ),
    ]
