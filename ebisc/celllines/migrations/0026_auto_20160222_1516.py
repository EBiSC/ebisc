# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0025_auto_20160222_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinediseasegenotype',
            name='carries_disease_phenotype_associated_variants',
            field=models.NullBooleanField(verbose_name='Cell line carries variants associated with the disease phenotype'),
        ),
        migrations.AddField(
            model_name='celllinediseasegenotype',
            name='variant_of_interest',
            field=models.NullBooleanField(verbose_name='Is the variant of interest, e.g. disease associated'),
        ),
    ]
