# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0004_cellline_disease_associated_phenotypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), null=True, verbose_name='Disease associated phenotypes', size=None),
        ),
    ]
