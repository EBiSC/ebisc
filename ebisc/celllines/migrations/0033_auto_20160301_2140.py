# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0032_auto_20160229_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinecharacterizationepipluriscore',
            name='epipluriscore_flag',
            field=models.NullBooleanField(verbose_name='EpiPluriScore flag'),
        ),
        migrations.AddField(
            model_name='celllinecharacterizationpluritest',
            name='pluritest_flag',
            field=models.NullBooleanField(verbose_name='Pluritest flag'),
        ),
    ]
