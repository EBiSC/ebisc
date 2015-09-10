# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0009_auto_20150907_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinebatch',
            name='certificate_of_analysis',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Certificate of analysis', blank=True),
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='certificate_of_analysis_md5',
            field=models.CharField(max_length=100, null=True, verbose_name='Certificate of analysis md5', blank=True),
        ),
    ]
