# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0014_auto_20160121_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllineinformationpack',
            name='clip_file',
            field=models.FileField(help_text=b'File name e.g. "UKBi005-A.CLIP.v1.pdf"', upload_to=ebisc.celllines.models.upload_to, verbose_name='CLIP file'),
        ),
        migrations.AlterField(
            model_name='celllineinformationpack',
            name='version',
            field=models.CharField(help_text=b'e.g. "v1"', max_length=10, verbose_name='CLIP version'),
        ),
    ]
