# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0034_celllinealiquot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinegeneticmodification',
            name='genetic_modification_flag',
            field=models.NullBooleanField(verbose_name='Genetic modification flag'),
        ),
    ]
