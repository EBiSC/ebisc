# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0063_auto_20170216_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllineethics',
            name='cell_line',
        ),
        migrations.AddField(
            model_name='cellline',
            name='has_genetic_modification',
            field=models.NullBooleanField(verbose_name='Genetic modification flag'),
        ),
        migrations.AlterField(
            model_name='cellline',
            name='name',
            field=models.CharField(unique=True, max_length=16, verbose_name='Cell line name'),
        ),
        migrations.DeleteModel(
            name='CelllineEthics',
        ),
    ]
