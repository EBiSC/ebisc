# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0003_auto_20150623_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='ecaccid',
            field=models.CharField(max_length=10, unique=True, null=True, verbose_name='ECACC ID', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='hescregid',
            field=models.CharField(max_length=10, unique=True, null=True, verbose_name='hESCreg ID', blank=True),
            preserve_default=True,
        ),
    ]
