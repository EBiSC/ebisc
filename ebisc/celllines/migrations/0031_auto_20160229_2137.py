# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0030_auto_20160229_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vectorfreereprogrammingfactor',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Vector free reprogram factor'),
        ),
    ]
