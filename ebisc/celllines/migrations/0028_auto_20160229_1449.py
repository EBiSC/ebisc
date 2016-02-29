# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0027_auto_20160229_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='factor',
            field=models.ManyToManyField(to='celllines.VectorFreeReprogrammingFactor', verbose_name='Vector-free reprogramming factor', blank=True),
        ),
    ]
