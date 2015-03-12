# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0011_auto_20150310_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='biosamplesid',
            field=models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinediseaseaddinfo',
            field=models.CharField(max_length=100, null=True, verbose_name='Cell line disease info', blank=True),
            preserve_default=True,
        ),
    ]
