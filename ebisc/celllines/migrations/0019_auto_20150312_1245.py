# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0018_celllinelab_mutagene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='celllinenamesynonyms',
            field=models.CharField(max_length=500, null=True, verbose_name='Cell line name synonyms', blank=True),
            preserve_default=True,
        ),
    ]
