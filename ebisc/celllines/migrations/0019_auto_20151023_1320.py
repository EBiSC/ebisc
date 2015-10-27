# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0018_auto_20151023_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinegenomeanalysis',
            name='data',
            field=models.CharField(max_length=100, null=True, verbose_name='Data', blank=True),
        ),
    ]
