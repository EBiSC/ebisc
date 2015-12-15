# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0004_auto_20151125_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinebatchimages',
            name='image_file',
        ),
        migrations.RemoveField(
            model_name='celllinebatchimages',
            name='image_md5',
        ),
        migrations.AddField(
            model_name='celllinebatchimages',
            name='image',
            field=models.ImageField(default='', upload_to=ebisc.celllines.models.upload_to, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinebatchimages',
            name='md5',
            field=models.CharField(default='', max_length=100, verbose_name='MD5'),
            preserve_default=False,
        ),
    ]
