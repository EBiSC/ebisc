# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0012_auto_20150623_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='ethnicity',
            field=models.CharField(max_length=100, null=True, verbose_name='Ethnicity', blank=True),
        ),
    ]
