# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0006_auto_20151207_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phenotypes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), null=True, verbose_name='Phenotypes', size=None),
        ),
    ]
