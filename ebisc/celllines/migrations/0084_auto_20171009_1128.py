# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0083_cellline_public_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='co2_concentration',
            field=models.CharField(help_text=b'e.g.: 5%', max_length=12, null=True, verbose_name='CO2 Concentration', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='culture_medium',
            field=models.CharField(help_text=b'e.g.: Essential E8', max_length=100, null=True, verbose_name='Medium', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='matrix',
            field=models.CharField(help_text=b'e.g.: Matrigel / Geltrex', max_length=100, null=True, verbose_name='Matrix', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='o2_concentration',
            field=models.CharField(help_text=b'e.g.: 18%', max_length=12, null=True, verbose_name='O2 Concentration', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='passage_method',
            field=models.CharField(help_text=b'e.g.: EDTA', max_length=100, null=True, verbose_name='Passage method', blank=True),
        ),
        migrations.AlterField(
            model_name='batchcultureconditions',
            name='temperature',
            field=models.CharField(help_text=b'e.g.: 37C', max_length=12, null=True, verbose_name='Temperature', blank=True),
        ),
    ]
