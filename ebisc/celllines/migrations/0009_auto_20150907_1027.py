# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0008_auto_20150907_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchcultureconditions',
            name='surface_coating',
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='co2_concentration',
            field=models.CharField(max_length=12, null=True, verbose_name='CO2 Concentration', blank=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='matrix',
            field=models.CharField(max_length=100, null=True, verbose_name='Matrix', blank=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='o2_concentration',
            field=models.CharField(max_length=12, null=True, verbose_name='O2 Concentration', blank=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='temperature',
            field=models.CharField(max_length=12, null=True, verbose_name='Temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='culture_medium',
            field=models.CharField(max_length=100, null=True, verbose_name='Medium', blank=True),
        ),
    ]
