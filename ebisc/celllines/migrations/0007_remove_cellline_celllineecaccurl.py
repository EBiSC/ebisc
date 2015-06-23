# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0006_auto_20150623_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellline',
            name='celllineecaccurl',
        ),
    ]
