# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0017_auto_20150312_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinelab',
            name='mutagene',
            field=models.CharField(max_length=100, verbose_name='Mutagene', blank=True),
            preserve_default=True,
        ),
    ]
