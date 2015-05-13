# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='synonyms',
            field=models.CharField(max_length=500, null=True, verbose_name='Synonyms', blank=True),
            preserve_default=True,
        ),
    ]
