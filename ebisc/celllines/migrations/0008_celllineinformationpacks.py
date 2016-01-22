# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0007_auto_20151207_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineInformationPacks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clip_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, verbose_name='Cell line information pack (CLIP)')),
                ('md5', models.CharField(max_length=100, verbose_name='CLIP md5')),
                ('version', models.CharField(max_length=10, null=True, verbose_name='CLIP version', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('cell_line', models.ForeignKey(related_name='clips', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line information pack',
                'verbose_name_plural': 'Cell line information packs',
            },
        ),
    ]
