# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0008_auto_20150623_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='providerdonorid',
        ),
        migrations.AddField(
            model_name='donor',
            name='provider_donor_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, verbose_name='Provider donor ids', size=None),
        ),
        migrations.AlterField(
            model_name='donor',
            name='countryoforigin',
            field=models.ForeignKey(verbose_name='Country of origin', blank=True, to='celllines.Country', null=True),
        ),
    ]
