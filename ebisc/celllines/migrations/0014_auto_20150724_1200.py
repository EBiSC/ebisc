# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0013_donor_ethnicity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinealiquot',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='celllinealiquot',
            name='status',
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='batch',
            field=models.ForeignKey(default=1, verbose_name='Cell line', to='celllines.CelllineBatch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='derived_from_aliqot',
            field=models.ForeignKey(verbose_name='Derived from aliquot', blank=True, to='celllines.CelllineAliquot', null=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='batch_id',
            field=models.CharField(default=1, max_length=10, verbose_name='Batch ID'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='celllinebatch',
            unique_together=set([('cell_line', 'batch_id')]),
        ),
        migrations.RemoveField(
            model_name='celllinebatch',
            name='status',
        ),
    ]
