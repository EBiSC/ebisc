# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0010_auto_20150910_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineBatchImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, verbose_name='Image file')),
                ('image_md5', models.CharField(max_length=100, verbose_name='Image file md5')),
                ('magnification', models.CharField(max_length=10, null=True, verbose_name='Magnification', blank=True)),
                ('time_point', models.CharField(max_length=100, null=True, verbose_name='Time point', blank=True)),
                ('batch', models.ForeignKey(related_name='images', verbose_name='Cell line Batch images', to='celllines.CelllineBatch')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line batch image',
                'verbose_name_plural': 'Cell line batch images',
            },
        ),
    ]
