# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0075_celllinecharacterizationgeneexpressionarray_celllinecharacterizationrnasequencing'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationDifferentiationPotency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('germ_layer', models.CharField(max_length=20, verbose_name='Germ layer', choices=[(b'endoderm', 'Endoderm'), (b'mesoderm', 'Mesoderm'), (b'ectoderm', 'Ectoderm')])),
                ('cell_line', models.ForeignKey(related_name='differentiation_potency_germ_layers', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['germ_layer'],
                'verbose_name': 'Germ layer',
                'verbose_name_plural': 'Germ layers',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationDifferentiationPotencyCellType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200, verbose_name='Name')),
                ('in_vivo_teratoma_flag', models.NullBooleanField(verbose_name='In vivo teratoma')),
                ('in_vitro_spontaneous_differentiation_flag', models.NullBooleanField(verbose_name='In vitro spontaneous differentiation')),
                ('in_vitro_directed_differentiation_flag', models.NullBooleanField(verbose_name='In vitro directed differentiation')),
                ('scorecard_flag', models.NullBooleanField(verbose_name='Scorecard')),
                ('other_flag', models.NullBooleanField(verbose_name='Other')),
                ('transcriptome_data', models.CharField(max_length=500, null=True, verbose_name='Link to transcriptome data', blank=True)),
                ('germ_layer', models.ForeignKey(related_name='germ_layer_cell_types', verbose_name='Germ layer', to='celllines.CelllineCharacterizationDifferentiationPotency')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Diferentiation potency cell type',
                'verbose_name_plural': 'Diferentiation potency cell types',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationDifferentiationPotencyCellTypeMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, verbose_name='Name')),
                ('expressed', models.NullBooleanField(verbose_name='Expressed')),
                ('cell_type', models.ForeignKey(related_name='germ_layer_cell_type_markers', verbose_name='Cell type', to='celllines.CelllineCharacterizationDifferentiationPotencyCellType')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Diferentiation potency cell type marker',
                'verbose_name_plural': 'Diferentiation potency cell type markers',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationDifferentiationPotencyMorphologyFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('cell_type', models.ForeignKey(related_name='germ_layer_cell_type_morphology_files', verbose_name='Cell type', to='celllines.CelllineCharacterizationDifferentiationPotencyCellType')),
            ],
            options={
                'ordering': ['cell_type'],
                'verbose_name': 'Diferentiation potency cell type morphology file',
                'verbose_name_plural': 'Diferentiation potency cell type morphology files',
            },
            bases=('celllines.depositordatafile',),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationDifferentiationPotencyProtocolFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('cell_type', models.ForeignKey(related_name='germ_layer_cell_type_protocol_files', verbose_name='Cell type', to='celllines.CelllineCharacterizationDifferentiationPotencyCellType')),
            ],
            options={
                'ordering': ['cell_type'],
                'verbose_name': 'Diferentiation potency cell type protocol file',
                'verbose_name_plural': 'Diferentiation potency cell type protocol files',
            },
            bases=('celllines.depositordatafile',),
        ),
    ]
