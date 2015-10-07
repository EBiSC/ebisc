# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0011_celllinebatchimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='primary_disease_diagnosis',
            field=models.CharField(max_length=12, null=True, verbose_name='Disease diagnosis', blank=True),
        ),
    ]
