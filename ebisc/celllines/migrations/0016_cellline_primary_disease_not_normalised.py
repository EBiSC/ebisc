# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0015_auto_20160121_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='primary_disease_not_normalised',
            field=models.CharField(max_length=100, null=True, verbose_name='Disease name - not normalised', blank=True),
        ),
    ]
