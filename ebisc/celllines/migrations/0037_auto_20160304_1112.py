# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0036_celllinegeneticmodification_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geneticmodificationisogenic',
            name='modified_sequence',
            field=models.CharField(max_length=500, null=True, verbose_name='Modified sequence', blank=True),
        ),
    ]
