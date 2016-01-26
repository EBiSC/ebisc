# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0016_cellline_primary_disease_not_normalised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='primary_disease_not_normalised',
            field=models.CharField(max_length=500, null=True, verbose_name='Disease name - not normalised', blank=True),
        ),
    ]
