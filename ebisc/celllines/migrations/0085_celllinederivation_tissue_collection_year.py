# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0084_auto_20171009_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinederivation',
            name='tissue_collection_year',
            field=models.CharField(max_length=50, null=True, verbose_name='Tissue collection year', blank=True),
        ),
    ]
