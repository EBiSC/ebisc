# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0077_auto_20170720_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinederivation',
            name='primary_cellline',
            field=models.CharField(max_length=500, null=True, verbose_name='Primary cell line', blank=True),
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='primary_cellline_vendor',
            field=models.CharField(max_length=500, null=True, verbose_name='Primary cell line vendor', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='expressed_silenced_file',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File - Integrating reprogramming vector expressed or silenced', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='expressed_silenced_file_enc',
            field=models.CharField(max_length=300, null=True, verbose_name='File enc - Integrating reprogramming vector expressed or silenced', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='vector_map_file',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File - vector map', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='vector_map_file_enc',
            field=models.CharField(max_length=300, null=True, verbose_name='File enc - vector map', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='expressed_silenced_file',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File - Non-integrating reprogramming vector expressed or silenced', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='expressed_silenced_file_enc',
            field=models.CharField(max_length=300, null=True, verbose_name='File enc - Non-integrating reprogramming vector expressed or silenced', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='vector_map_file',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File - vector map', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='vector_map_file_enc',
            field=models.CharField(max_length=300, null=True, verbose_name='File enc - vector map', blank=True),
        ),
    ]
