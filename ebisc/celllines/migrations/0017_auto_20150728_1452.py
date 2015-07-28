# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0016_auto_20150728_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batchcultureconditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passagemethod', models.CharField(max_length=100, null=True, verbose_name='Passage method', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Batch culture conditions',
                'verbose_name_plural': 'Batch culture conditions',
            },
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='cells_per_vial',
            field=models.CharField(max_length=50, null=True, verbose_name='Cells per vial', blank=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='passage_number',
            field=models.IntegerField(null=True, verbose_name='Passage number', blank=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='vials_at_roslin',
            field=models.IntegerField(null=True, verbose_name='Vials at Central facility', blank=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='vials_shipped_to_ecacc',
            field=models.IntegerField(null=True, verbose_name='Vials shipped to ECACC', blank=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='vials_shipped_to_fraunhoffer',
            field=models.IntegerField(null=True, verbose_name='Vials shipped to Fraunhoffer', blank=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='batch',
            field=models.OneToOneField(verbose_name='Batch', to='celllines.CelllineBatch'),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='culture_medium',
            field=models.ForeignKey(verbose_name='Culture medium', blank=True, to='celllines.CultureMedium', null=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='surface_coating',
            field=models.ForeignKey(verbose_name='Matrix', blank=True, to='celllines.SurfaceCoating', null=True),
        ),
    ]
