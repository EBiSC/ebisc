# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0005_auto_20151130_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='molecule',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
    ]
