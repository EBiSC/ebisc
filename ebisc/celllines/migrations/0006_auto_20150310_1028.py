# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0005_auto_20150310_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celltype',
            options={'ordering': ['celltype'], 'verbose_name': 'Cell type', 'verbose_name_plural': 'Cell types'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['country'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(unique=True, max_length=45, verbose_name='Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='countrycode',
            field=models.CharField(max_length=3, unique=True, null=True, verbose_name='Country code', blank=True),
            preserve_default=True,
        ),
    ]
