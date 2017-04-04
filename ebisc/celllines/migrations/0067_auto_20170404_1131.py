# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0066_auto_20170329_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='karyotype_file',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File', blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='karyotype_file_enc',
            field=models.CharField(max_length=300, null=True, verbose_name='File enc', blank=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='karyotype_method',
            field=models.CharField(max_length=100, null=True, verbose_name='Karyotype method', blank=True),
        ),
    ]
