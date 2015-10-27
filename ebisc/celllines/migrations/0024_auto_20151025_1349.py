# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0023_auto_20151025_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturemediumother',
            name='protein_source',
            field=models.CharField(max_length=45, null=True, verbose_name='Protein source', blank=True),
        ),
        migrations.DeleteModel(
            name='ProteinSource',
        ),
    ]
