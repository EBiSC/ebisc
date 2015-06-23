# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0005_cellline_derivation_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Celllinecomments',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='celllinecomments',
        ),
        migrations.AddField(
            model_name='cellline',
            name='comments',
            field=models.TextField(null=True, verbose_name='Comments', blank=True),
            preserve_default=True,
        ),
    ]
