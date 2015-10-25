# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0021_auto_20151023_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='culture_history',
            field=models.NullBooleanField(default=None, verbose_name='Culture history (methods used)'),
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='passage_history',
            field=models.NullBooleanField(default=None, verbose_name='Passage history (back to reprogramming)'),
        ),
    ]
