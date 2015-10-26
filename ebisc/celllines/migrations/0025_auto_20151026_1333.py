# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0024_auto_20151025_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinederivation',
            name='primary_cell_developmental_stage',
            field=models.CharField(max_length=45, null=True, verbose_name='Primary cell developmental stage', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='tissue_procurement_location',
            field=models.CharField(max_length=45, null=True, verbose_name='Location of primary tissue procurement', blank=True),
        ),
        migrations.DeleteModel(
            name='PrimaryCellDevelopmentalStage',
        ),
        migrations.DeleteModel(
            name='TissueLocation',
        ),
    ]
