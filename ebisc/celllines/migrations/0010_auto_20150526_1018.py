# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0009_auto_20150526_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='certificate_of_analysis_passage_number',
            field=models.CharField(max_length=10, null=True, verbose_name='Certificate of analysis passage number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinekaryotype',
            name='passage_number',
            field=models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True),
            preserve_default=True,
        ),
    ]
