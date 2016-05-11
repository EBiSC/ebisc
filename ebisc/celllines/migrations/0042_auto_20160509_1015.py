# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0041_auto_20160427_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinealiquot',
            name='derived_from_aliqot',
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='derived_from',
            field=models.CharField(max_length=12, null=True, verbose_name='Biosamples ID of sample from which the vial was derived', blank=True),
        ),
    ]
