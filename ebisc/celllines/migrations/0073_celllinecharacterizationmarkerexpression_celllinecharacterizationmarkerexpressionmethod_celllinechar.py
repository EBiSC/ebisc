# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0072_celllinecharacterizationepipluriscorefile_celllinecharacterizationhpscscorecard_celllinecharacteriza'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationMarkerExpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marker', models.CharField(max_length=100, verbose_name='Marker')),
                ('expressed', models.NullBooleanField(verbose_name='Expressed')),
                ('cell_line', models.ForeignKey(related_name='undifferentiated_marker_expression', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Undifferentiated cells - marker expression',
                'verbose_name_plural': 'Undifferentiated cells - marker expressions',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationMarkerExpressionMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='Method name')),
                ('marker_expression', models.ForeignKey(related_name='marker_expression_method', verbose_name='Marker expression', to='celllines.CelllineCharacterizationMarkerExpression')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Marker expression method',
                'verbose_name_plural': 'Marker expression methods',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationMarkerExpressionMethodFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('marker_expression_method', models.ForeignKey(related_name='marker_expression_method_files', verbose_name='Marker expression method', to='celllines.CelllineCharacterizationMarkerExpressionMethod')),
            ],
            options={
                'ordering': ['marker_expression_method'],
                'verbose_name': 'Marker expression method file',
                'verbose_name_plural': 'Marker expression method files',
            },
            bases=('celllines.depositordatafile',),
        ),
    ]
