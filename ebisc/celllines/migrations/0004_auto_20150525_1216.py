# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0003_auto_20150525_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinepublication',
            name='reference_type',
            field=models.CharField(max_length=100, verbose_name='Type', choices=[(b'pubmed', b'PubMed')]),
            preserve_default=True,
        ),
    ]
