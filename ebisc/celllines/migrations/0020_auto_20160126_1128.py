# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0019_celllinecharacterizationepipluriscore_celllinecharacterizationpluritest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='icdcode',
            field=models.CharField(max_length=300, unique=True, null=True, verbose_name='DOID', blank=True),
        ),
    ]
