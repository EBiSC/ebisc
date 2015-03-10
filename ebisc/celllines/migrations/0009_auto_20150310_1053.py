# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0008_celllinechecklist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='strfplocus',
            options={'ordering': [], 'verbose_name': 'STR FP locus', 'verbose_name_plural': 'STR FP loci'},
        ),
        migrations.AlterField(
            model_name='strfplocus',
            name='strfplocus',
            field=models.CharField(max_length=45, verbose_name='STR FP locus', blank=True),
            preserve_default=True,
        ),
    ]
