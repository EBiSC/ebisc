# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0042_auto_20160509_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllineinformationpack',
            options={'ordering': ['-updated'], 'verbose_name': 'Cell line information pack', 'verbose_name_plural': 'Cell line information packs'},
        ),
        migrations.AlterUniqueTogether(
            name='celllineinformationpack',
            unique_together=set([('cell_line', 'version')]),
        ),
    ]
