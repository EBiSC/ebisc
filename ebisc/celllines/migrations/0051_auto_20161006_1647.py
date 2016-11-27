# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0050_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinealiquot',
            name='derived_from',
            field=models.CharField(max_length=100, null=True, verbose_name='Biosamples ID of sample from which the vial was derived', blank=True),
        ),
    ]
