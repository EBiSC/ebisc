# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0012_auto_20150312_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinecollection',
            name='celllinecollectionupdatedby',
            field=models.CharField(max_length=45, null=True, verbose_name='Cell line collection updated by', blank=True),
            preserve_default=True,
        ),
    ]
