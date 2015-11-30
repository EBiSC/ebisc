# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0002_auto_20151120_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='available_for_sale',
            field=models.NullBooleanField(verbose_name='Available for sale'),
        ),
    ]
