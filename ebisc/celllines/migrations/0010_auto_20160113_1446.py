# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0009_auto_20160113_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='validated',
            field=models.CharField(default=b'5', max_length=50, verbose_name='Cell line data validation', choices=[(b'1', 'Validated, visible'), (b'2', 'Validated, not visible'), (b'3', 'Unvalidated'), (b'5', 'Name registered')]),
        ),
    ]
