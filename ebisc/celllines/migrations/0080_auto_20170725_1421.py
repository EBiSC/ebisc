# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0079_celllinevectorfreereprogrammingfactor_celllinevectorfreereprogrammingfactormolecule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='factors',
        ),
        migrations.DeleteModel(
            name='CelllineVectorFreeReprogrammingFactors',
        ),
    ]
