# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0003_cellline_available_for_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='access_and_use_agreement',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Access and use agreement (AUA)', blank=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='access_and_use_agreement_md5',
            field=models.CharField(max_length=100, null=True, verbose_name='Access and use agreement md5', blank=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='access_and_use_agreement_participant',
            field=models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Access and use agreement for participants (prAUA)', blank=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='access_and_use_agreement_participant_md5',
            field=models.CharField(max_length=100, null=True, verbose_name='Access and use agreement for participants md5', blank=True),
        ),
    ]
