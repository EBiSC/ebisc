# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0054_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinestatus',
            name='comment',
            field=models.TextField(help_text=b'Optional unless you are recalling or withdrawing a line. In that case you must provide a reason for the recall/withdrawal.', null=True, verbose_name='Comment', blank=True),
        ),
    ]
