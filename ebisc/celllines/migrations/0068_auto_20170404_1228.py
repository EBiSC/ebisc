# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0067_auto_20170404_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donordisease',
            name='disease_stage',
            field=models.CharField(max_length=1000, null=True, verbose_name='Disease stage', blank=True),
        ),
    ]
