# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0070_auto_20170418_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellline',
            name='clinical_information',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='family_history',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='medical_history',
        ),
        migrations.AddField(
            model_name='donor',
            name='clinical_information',
            field=models.CharField(max_length=500, null=True, verbose_name='Clinical information', blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='family_history',
            field=models.CharField(max_length=500, null=True, verbose_name='Family history', blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='medical_history',
            field=models.CharField(max_length=500, null=True, verbose_name='Medical history', blank=True),
        ),
    ]
