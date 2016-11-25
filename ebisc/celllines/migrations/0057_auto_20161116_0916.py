# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0056_remove_cellline_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease_not_normalised', models.CharField(max_length=500, null=True, verbose_name='Disease name - not normalised', blank=True)),
                ('primary_disease', models.BooleanField(default=False, verbose_name='Primary disease')),
                ('disease_stage', models.CharField(max_length=100, null=True, verbose_name='Disease stage', blank=True)),
                ('affected_status', models.CharField(max_length=12, null=True, verbose_name='Affected status', blank=True)),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['disease'],
                'verbose_name': 'Cell line disease',
                'verbose_name_plural': 'Cell line diseases',
            },
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['xpurl'], 'verbose_name': 'Disease', 'verbose_name_plural': 'Diseases'},
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='affected_status',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='primary_disease',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='primary_disease_diagnosis',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='primary_disease_not_normalised',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='primary_disease_stage',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='icdcode',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='purl',
        ),
        migrations.AddField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='xpurl',
            field=models.URLField(default='', verbose_name='Purl'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='disease_associated_phenotypes',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=500), null=True, verbose_name='Disease associated phenotypes', blank=True),
        ),
        migrations.AddField(
            model_name='celllinedisease',
            name='cell_line',
            field=models.ForeignKey(related_name='diseases', verbose_name='Cell line', to='celllines.Cellline'),
        ),
        migrations.AddField(
            model_name='celllinedisease',
            name='disease',
            field=models.ForeignKey(verbose_name='Diagnosed disease', blank=True, to='celllines.Disease', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='celllinedisease',
            unique_together=set([('cell_line', 'disease', 'disease_not_normalised')]),
        ),
    ]
