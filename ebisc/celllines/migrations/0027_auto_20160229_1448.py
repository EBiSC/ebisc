# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0026_auto_20160222_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vectorfreereprogrammingfactor',
            name='reference_id',
        ),
        migrations.RemoveField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='factor',
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='factor',
            field=models.ManyToManyField(to='celllines.VectorFreeReprogrammingFactor', null=True, verbose_name='Vector-free reprogramming factor', blank=True),
        ),
        migrations.AlterField(
            model_name='vectorfreereprogrammingfactor',
            name='vector_free_reprogramming_factor',
            field=models.CharField(max_length=50, verbose_name='Vector free reprogram factor', blank=True),
        ),
    ]
