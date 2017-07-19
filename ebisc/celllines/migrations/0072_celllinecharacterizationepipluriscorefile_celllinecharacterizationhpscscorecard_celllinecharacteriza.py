# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0071_auto_20170418_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationHpscScorecard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('self_renewal', models.NullBooleanField(verbose_name='Self renewal')),
                ('endoderm', models.NullBooleanField(verbose_name='Endoderm')),
                ('mesoderm', models.NullBooleanField(verbose_name='Mesoderm')),
                ('ectoderm', models.NullBooleanField(verbose_name='Ectoderm')),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line hPSC Scorecard',
                'verbose_name_plural': 'Cell line hPSC Scorecards',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DepositorDataFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_doc', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File', blank=True)),
                ('file_enc', models.CharField(max_length=300, null=True, verbose_name='File enc', blank=True)),
                ('file_description', models.TextField(null=True, verbose_name='File description', blank=True)),
            ],
            options={
                'ordering': ['file_enc'],
                'verbose_name': 'Depositor data file',
                'verbose_name_plural': 'Depositor data files',
            },
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationEpipluriscoreFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('epipluriscore', models.ForeignKey(related_name='epipluriscore_files', verbose_name='Cell line EpiPluriScore', to='celllines.CelllineCharacterizationEpipluriscore')),
            ],
            options={
                'ordering': ['epipluriscore'],
                'verbose_name': 'Cell line EpiPluriScore file',
                'verbose_name_plural': 'Cell line EpiPluriScore files',
            },
            bases=('celllines.depositordatafile',),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationHpscScorecardReport',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('hpsc_scorecard', models.ForeignKey(related_name='hpsc_scorecard_reports', verbose_name='Cell line hPSC Scorecard', to='celllines.CelllineCharacterizationHpscScorecard')),
            ],
            options={
                'ordering': ['hpsc_scorecard'],
                'verbose_name': 'Cell line hPSC Scorecard report',
                'verbose_name_plural': 'Cell line hPSC Scorecard reports',
            },
            bases=('celllines.depositordatafile',),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationHpscScorecardScorecard',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('hpsc_scorecard', models.ForeignKey(related_name='hpsc_scorecard_files', verbose_name='Cell line hPSC Scorecard', to='celllines.CelllineCharacterizationHpscScorecard')),
            ],
            options={
                'ordering': ['hpsc_scorecard'],
                'verbose_name': 'Cell line hPSC Scorecard scorecard',
                'verbose_name_plural': 'Cell line hPSC Scorecard scorecards',
            },
            bases=('celllines.depositordatafile',),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationPluritestFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('pluritest', models.ForeignKey(related_name='pluritest_files', verbose_name='Cell line pluritest', to='celllines.CelllineCharacterizationPluritest')),
            ],
            options={
                'ordering': ['pluritest'],
                'verbose_name': 'Cell line Pluritest file',
                'verbose_name_plural': 'Cell line Pluritest files',
            },
            bases=('celllines.depositordatafile',),
        ),
        migrations.CreateModel(
            name='CelllineCharacterizationUndifferentiatedMorphologyFile',
            fields=[
                ('depositordatafile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.DepositorDataFile')),
                ('cell_line', models.ForeignKey(related_name='undifferentiated_morphology_files', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line undifferentiated cells morphology file',
                'verbose_name_plural': 'Cell line undifferentiated cells morphology files',
            },
            bases=('celllines.depositordatafile',),
        ),
    ]
