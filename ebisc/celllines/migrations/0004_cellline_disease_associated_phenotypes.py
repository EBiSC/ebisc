# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0003_donor_karyotype'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, verbose_name='Disease associated phenotypes', size=None),
        ),
    ]
