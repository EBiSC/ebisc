# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0078_auto_20170721_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineVectorFreeReprogrammingFactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.ForeignKey(related_name='derivation_vector_free_reprogramming_factors', verbose_name='Cell line', to='celllines.Cellline')),
                ('factor', models.ForeignKey(verbose_name='Vector-free reprogramming factor', blank=True, to='celllines.VectorFreeReprogrammingFactor')),
            ],
            options={
                'verbose_name': 'Cell line Vector-free Programming Factor',
                'verbose_name_plural': 'Cell line Vector-free Programming Factors',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineVectorFreeReprogrammingFactorMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='Molecule name')),
                ('reprogramming_factor', models.ForeignKey(related_name='reprogramming_factor_molecules', verbose_name='Cell line reprogramming factor', to='celllines.CelllineVectorFreeReprogrammingFactor')),
            ],
            options={
                'verbose_name': 'Cell line Vector-free Programming Factor molecule',
                'verbose_name_plural': 'Cell line Vector-free Programming Factor molecules',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
