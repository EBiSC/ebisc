# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0018_auto_20150729_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='cellline_alternate_names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), null=True, verbose_name='Cell line name alternate names', size=None),
        ),
    ]
