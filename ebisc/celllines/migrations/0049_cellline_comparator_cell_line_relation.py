# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0048_auto_20160923_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='comparator_cell_line_relation',
            field=models.CharField(max_length=100, null=True, verbose_name='Comparator cell line relation', blank=True),
        ),
    ]
