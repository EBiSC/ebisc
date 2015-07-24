# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0014_auto_20150724_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinebatch',
            name='batch_id',
            field=models.CharField(max_length=12, verbose_name='Batch ID'),
        ),
    ]
