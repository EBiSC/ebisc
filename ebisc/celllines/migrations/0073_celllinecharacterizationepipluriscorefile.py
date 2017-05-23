# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0072_celllinecharacterizationpluritestfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationEpipluriscoreFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('epipluriscore_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File', blank=True)),
                ('epipluriscore_file_enc', models.CharField(max_length=300, null=True, verbose_name='File enc', blank=True)),
                ('epipluriscore_file_description', models.TextField(null=True, verbose_name='File description', blank=True)),
                ('epipluriscore', models.ForeignKey(related_name='epipluriscore_files', verbose_name='Cell line EpiPluriScore', to='celllines.CelllineCharacterizationEpipluriscore')),
            ],
            options={
                'ordering': ['epipluriscore'],
                'verbose_name': 'Cell line EpiPluriScore file',
                'verbose_name_plural': 'Cell line EpiPluriScore files',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
