# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0052_auto_20161014_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='current_status',
            field=models.ForeignKey(blank=True, to='celllines.CelllineStatus', null=True),
        ),
    ]
