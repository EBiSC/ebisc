# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0045_auto_20160708_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='biosamples_id',
            field=models.CharField(unique=True, max_length=100, verbose_name='Biosamples ID'),
        ),
        migrations.AlterField(
            model_name='celllinealiquot',
            name='biosamples_id',
            field=models.CharField(unique=True, max_length=100, verbose_name='Biosamples ID'),
        ),
        migrations.AlterField(
            model_name='celllinebatch',
            name='biosamples_id',
            field=models.CharField(unique=True, max_length=100, verbose_name='Biosamples ID'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='biosamples_id',
            field=models.CharField(unique=True, max_length=100, verbose_name='Biosamples ID'),
        ),
    ]
