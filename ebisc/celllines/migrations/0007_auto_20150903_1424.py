# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0006_auto_20150903_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='affected_status',
            field=models.CharField(max_length=12, null=True, verbose_name='Affected status', blank=True),
        ),
    ]
