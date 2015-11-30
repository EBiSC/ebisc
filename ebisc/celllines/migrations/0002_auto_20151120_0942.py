# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='purl',
            field=models.URLField(max_length=300, null=True, verbose_name='Purl', blank=True),
        ),
    ]
