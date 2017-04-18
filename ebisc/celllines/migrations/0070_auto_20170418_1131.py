# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0069_auto_20170418_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinediseasegenotype',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingrsnumber',
            name='disease_genotype',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingsnp',
            name='disease_genotype',
        ),
        migrations.RemoveField(
            model_name='donorgenotype',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='donorgenotypingrsnumber',
            name='donor_genotype',
        ),
        migrations.RemoveField(
            model_name='donorgenotypingsnp',
            name='donor_genotype',
        ),
        migrations.DeleteModel(
            name='CelllineDiseaseGenotype',
        ),
        migrations.DeleteModel(
            name='CelllineGenotypingRsNumber',
        ),
        migrations.DeleteModel(
            name='CelllineGenotypingSNP',
        ),
        migrations.DeleteModel(
            name='DonorGenotype',
        ),
        migrations.DeleteModel(
            name='DonorGenotypingRsNumber',
        ),
        migrations.DeleteModel(
            name='DonorGenotypingSNP',
        ),
    ]
