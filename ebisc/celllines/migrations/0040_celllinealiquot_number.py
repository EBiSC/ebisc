# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0039_celllinebatch_batch_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinealiquot',
            name='number',
            field=models.CharField(max_length=10, null=True, verbose_name='Number', blank=True),
        ),
    ]
