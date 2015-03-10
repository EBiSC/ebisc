# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0003_auto_20150310_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='icdcode',
            field=models.CharField(max_length=10, unique=True, null=True, verbose_name='Icdcode', blank=True),
            preserve_default=True,
        ),
    ]
