# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0004_auto_20150525_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='celllinepublication',
            old_name='cellline',
            new_name='cell_line',
        ),
        migrations.AlterUniqueTogether(
            name='celllinepublication',
            unique_together=set([('cell_line', 'reference_url')]),
        ),
    ]
