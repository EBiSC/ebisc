# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0082_auto_20170918_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='public_notes',
            field=models.TextField(null=True, verbose_name='Public notes', blank=True),
        ),
    ]
