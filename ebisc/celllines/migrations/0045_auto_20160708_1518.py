# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0044_auto_20160708_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='disease',
            field=models.CharField(max_length=200, verbose_name='Disease', blank=True),
        ),
    ]
