# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0047_auto_20160916_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='comparator_cell_line',
            field=models.ForeignKey(related_name='comparator_cell_lines', verbose_name='Comparator cell line', blank=True, to='celllines.Cellline', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='derived_from',
            field=models.ForeignKey(related_name='derived_cell_lines', verbose_name='Derived from cell line', blank=True, to='celllines.Cellline', null=True),
        ),
    ]
