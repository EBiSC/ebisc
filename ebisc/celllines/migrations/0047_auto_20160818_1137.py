# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0046_auto_20160818_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['purl'], 'verbose_name': 'Disease', 'verbose_name_plural': 'Diseases'},
        ),
        migrations.RenameField(
            model_name='disease',
            old_name='xpurl',
            new_name='purl',
        ),
    ]
