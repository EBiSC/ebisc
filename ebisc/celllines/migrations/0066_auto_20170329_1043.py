# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0065_auto_20170329_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinegenomeanalysisfile',
            name='vcf_file_description',
            field=models.CharField(max_length=500, null=True, verbose_name='VCF File description', blank=True),
        ),
        migrations.AddField(
            model_name='donorgenomeanalysisfile',
            name='vcf_file_description',
            field=models.CharField(max_length=500, null=True, verbose_name='VCF File description', blank=True),
        ),
    ]
