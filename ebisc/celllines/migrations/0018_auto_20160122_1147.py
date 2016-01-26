# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0017_auto_20160122_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinederivation',
            name='primary_cell_type_not_normalised',
            field=models.CharField(max_length=100, null=True, verbose_name='Primary cell type name - not normalised', blank=True),
        ),
        migrations.AddField(
            model_name='celltype',
            name='purl',
            field=models.URLField(max_length=300, null=True, verbose_name='Purl', blank=True),
        ),
    ]
