# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0004_auto_20150623_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='derivation_country',
            field=models.ForeignKey(verbose_name='Derivation country', blank=True, to='celllines.Country', null=True),
            preserve_default=True,
        ),
    ]
