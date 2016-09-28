# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0047_auto_20160916_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='primary_disease',
            field=models.ForeignKey(related_name='primary_disease', verbose_name='Diagnosed disease', blank=True, to='celllines.Disease', null=True),
        ),
    ]
