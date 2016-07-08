# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0043_auto_20160610_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='synonyms',
            field=models.CharField(max_length=2000, null=True, verbose_name='Synonyms', blank=True),
        ),
    ]
