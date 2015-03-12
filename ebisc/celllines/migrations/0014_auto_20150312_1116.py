# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0013_auto_20150312_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinecollection',
            options={'ordering': ['id'], 'verbose_name': 'Cell line collection', 'verbose_name_plural': 'Cell line collections'},
        ),
        migrations.AlterModelOptions(
            name='tissuesource',
            options={'ordering': ['tissuesource'], 'verbose_name': 'Tissue source', 'verbose_name_plural': 'Tissue sources'},
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinetissuetreatment',
            field=models.ForeignKey(blank=True, to='celllines.Clinicaltreatmentb4donation', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecollection',
            name='celllinecollectionupdate',
            field=models.DateField(null=True, verbose_name='Updated', blank=True),
            preserve_default=True,
        ),
    ]
