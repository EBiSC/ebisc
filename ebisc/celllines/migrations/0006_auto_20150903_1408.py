# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0005_auto_20150903_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='affected_status',
            field=models.NullBooleanField(verbose_name='Affected status'),
        ),
        migrations.AddField(
            model_name='cellline',
            name='clinical_information',
            field=models.CharField(max_length=500, null=True, verbose_name='Clinical information', blank=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='family_history',
            field=models.CharField(max_length=500, null=True, verbose_name='Family history', blank=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='medical_history',
            field=models.CharField(max_length=500, null=True, verbose_name='Medical history', blank=True),
        ),
    ]
