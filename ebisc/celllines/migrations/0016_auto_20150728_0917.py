# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0015_auto_20150724_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinealiquot',
            name='batch',
            field=models.ForeignKey(related_name='aliquot', verbose_name='Cell line', to='celllines.CelllineBatch'),
        ),
        migrations.AlterField(
            model_name='celllinebatch',
            name='cell_line',
            field=models.ForeignKey(related_name='batch', verbose_name='Cell line', to='celllines.Cellline'),
        ),
    ]
