# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0013_auto_20160121_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineInformationPack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=10, verbose_name='CLIP version')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('clip_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, verbose_name='Cell line information pack (CLIP)')),
                ('md5', models.CharField(max_length=100, verbose_name='CLIP md5')),
                ('cell_line', models.ForeignKey(related_name='clips', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line information pack',
                'verbose_name_plural': 'Cell line information packs',
            },
        ),
        migrations.RemoveField(
            model_name='celllineinformationpacks',
            name='cell_line',
        ),
        migrations.DeleteModel(
            name='CelllineInformationPacks',
        ),
    ]
