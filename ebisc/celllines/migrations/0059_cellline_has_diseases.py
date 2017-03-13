# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0058_auto_20161125_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='has_diseases',
            field=models.NullBooleanField(verbose_name='Has diseases'),
        ),
    ]
