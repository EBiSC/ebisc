# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0007_auto_20150903_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinebatch',
            name='cells_per_vial',
        ),
        migrations.RemoveField(
            model_name='celllinebatch',
            name='passage_number',
        ),
    ]
