# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0005_auto_20150525_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integratingvector',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Integrating vector'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nonintegratingvector',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Non-integrating vector'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transposon',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Transposon', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='virus',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Virus'),
            preserve_default=True,
        ),
    ]
