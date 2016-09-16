# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0046_auto_20160905_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='phenotypes',
        ),
        migrations.AddField(
            model_name='cellline',
            name='non_disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=700), null=True, verbose_name='Non-disease associated phenotypes', blank=True),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=700), null=True, verbose_name='Disease associated phenotypes', blank=True),
        ),
    ]
