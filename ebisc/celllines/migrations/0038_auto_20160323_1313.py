# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0037_auto_20160304_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinealiquot',
            options={'ordering': ['name'], 'verbose_name': 'Cell line aliquot', 'verbose_name_plural': 'Cell line aliquotes'},
        ),
    ]
