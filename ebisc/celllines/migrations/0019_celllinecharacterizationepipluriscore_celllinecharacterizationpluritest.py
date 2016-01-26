# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0018_auto_20160122_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationEpipluriscore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.CharField(max_length=10, null=True, verbose_name='Pluripotency score', blank=True)),
                ('marker_mcpg', models.NullBooleanField(verbose_name='Marker mCpG')),
                ('marker_OCT4', models.NullBooleanField(verbose_name='Marker OCT4')),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line characterization Epipluri score',
                'verbose_name_plural': 'Cell line characterization Epipluri scores',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationPluritest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pluripotency_score', models.CharField(max_length=10, null=True, verbose_name='Pluripotency score', blank=True)),
                ('novelty_score', models.CharField(max_length=10, null=True, verbose_name='Novelty score', blank=True)),
                ('microarray_url', models.URLField(max_length=300, null=True, verbose_name='Microarray data link', blank=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line characterization Pluritest',
                'verbose_name_plural': 'Cell line characterization Pluritests',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
