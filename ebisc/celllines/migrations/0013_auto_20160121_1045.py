# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0012_cellline_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllineinformationpacks',
            name='version',
            field=models.CharField(max_length=10, verbose_name='CLIP version'),
        ),
    ]
