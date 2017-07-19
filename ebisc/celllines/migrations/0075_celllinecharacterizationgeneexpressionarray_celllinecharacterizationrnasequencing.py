# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0074_celllinecharacterizationmarkerexpression_marker_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationGeneExpressionArray',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_url', models.CharField(default=b'', max_length=500, verbose_name='Gene Expression Array data link', blank=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['data_url'],
                'verbose_name': 'Link to Gene Expression Array data',
                'verbose_name_plural': 'Links to Gene Expression Array data',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationRNASequencing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_url', models.CharField(default=b'', max_length=500, verbose_name='RNA Sequencing data link', blank=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['data_url'],
                'verbose_name': 'Link to RNA Sequencing data',
                'verbose_name_plural': 'Links to RNA Sequencing data',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
