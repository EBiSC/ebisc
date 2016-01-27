# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0020_auto_20160126_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=500), null=True, verbose_name='Disease associated phenotypes', blank=True),
        ),
    ]
