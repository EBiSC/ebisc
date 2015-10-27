# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0020_auto_20151023_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinekaryotype',
            name='karyotype_method',
            field=models.CharField(max_length=100, null=True, verbose_name='Karyotype method', blank=True),
        ),
        migrations.DeleteModel(
            name='KaryotypeMethod',
        ),
    ]
