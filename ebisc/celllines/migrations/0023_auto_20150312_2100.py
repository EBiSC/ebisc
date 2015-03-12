# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0022_auto_20150312_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinechecklist',
            name='virustesting',
            field=models.BooleanField(default=False, verbose_name='Virus testing'),
            preserve_default=True,
        ),
    ]
