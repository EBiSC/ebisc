# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0017_auto_20150728_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinealiquot',
            name='batch',
            field=models.ForeignKey(related_name='aliquots', verbose_name='Cell line', to='celllines.CelllineBatch'),
        ),
        migrations.AlterField(
            model_name='celllinebatch',
            name='cell_line',
            field=models.ForeignKey(related_name='batches', verbose_name='Cell line', to='celllines.Cellline'),
        ),
    ]
