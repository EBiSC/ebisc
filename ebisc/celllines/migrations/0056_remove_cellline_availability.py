# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0055_auto_20161020_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellline',
            name='availability',
        ),
    ]
