# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0068_auto_20170404_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinegeneticmodification',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockin',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockin',
            name='target_genes',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockin',
            name='transgenes',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockin',
            name='transposon',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockin',
            name='virus',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockout',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockout',
            name='target_genes',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockout',
            name='transposon',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationgeneknockout',
            name='virus',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationisogenic',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationisogenic',
            name='target_locus',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationtransgeneexpression',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationtransgeneexpression',
            name='genes',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationtransgeneexpression',
            name='transposon',
        ),
        migrations.RemoveField(
            model_name='geneticmodificationtransgeneexpression',
            name='virus',
        ),
        migrations.DeleteModel(
            name='CelllineGeneticModification',
        ),
        migrations.DeleteModel(
            name='GeneticModificationGeneKnockIn',
        ),
        migrations.DeleteModel(
            name='GeneticModificationGeneKnockOut',
        ),
        migrations.DeleteModel(
            name='GeneticModificationIsogenic',
        ),
        migrations.DeleteModel(
            name='GeneticModificationTransgeneExpression',
        ),
    ]
