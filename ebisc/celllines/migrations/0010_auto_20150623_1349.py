# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0009_auto_20150623_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllineintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinenonintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
    ]
