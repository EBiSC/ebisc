# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0029_auto_20160229_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='celllinevectorfreereprogrammingfactors',
            old_name='factor',
            new_name='factors',
        ),
    ]
