# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0035_celllinegeneticmodification_genetic_modification_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinegeneticmodification',
            name='types',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=50), null=True, verbose_name='Types of modification', blank=True),
        ),
    ]
