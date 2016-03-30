# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0033_auto_20160301_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinealiquot',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name', blank=True),
        ),
    ]
