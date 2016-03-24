# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0038_auto_20160323_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinebatch',
            name='batch_type',
            field=models.CharField(default=b'unknown', max_length=50, verbose_name='Batch type', choices=[(b'depositor', 'Depositor Expansion'), (b'central_facility', 'Central Facility Expansion'), (b'unknown', 'Unknown')]),
        ),
    ]
