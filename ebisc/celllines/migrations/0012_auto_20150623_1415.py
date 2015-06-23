# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0011_celllinevectorfreereprogrammingfactors'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellLineDifferentiationPotency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=5, verbose_name='Passage number', blank=True)),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
                ('germ_layer', models.ForeignKey(verbose_name='Germ layer', blank=True, to='celllines.Germlayer', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency',
                'verbose_name_plural': 'Cell line differentiation potencies',
            },
        ),
        migrations.CreateModel(
            name='CellLineDifferentiationPotencyMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line_differentiation_potency', models.ForeignKey(verbose_name='Cell line differentiation potency', blank=True, to='celllines.CellLineDifferentiationPotency', null=True)),
                ('morphology_method', models.ForeignKey(verbose_name='Morphology method', blank=True, to='celllines.Morphologymethod', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency marker',
                'verbose_name_plural': 'Cell line differentiation potency markers',
            },
        ),
        migrations.CreateModel(
            name='CellLineDifferentiationPotencyMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line_differentiation_potency_marker', models.ForeignKey(verbose_name='Cell line differentiation potency marker', blank=True, to='celllines.CellLineDifferentiationPotencyMarker', null=True)),
                ('molecule', models.ForeignKey(verbose_name='Molecule', blank=True, to='celllines.Molecule', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency molecule',
                'verbose_name_plural': 'Cell line differentiation potency molecules',
            },
        ),
        migrations.CreateModel(
            name='CellLineMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line marker',
                'verbose_name_plural': 'Cell line markers',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Marker', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Marker',
                'verbose_name_plural': 'Markers',
            },
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='marker',
            field=models.ForeignKey(verbose_name='Marker', blank=True, to='celllines.Marker', null=True),
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='morphology_method',
            field=models.ForeignKey(verbose_name='Morphology method', blank=True, to='celllines.Morphologymethod', null=True),
        ),
    ]
