# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0071_auto_20170418_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationPluritestFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pluritest_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File', blank=True)),
                ('pluritest_file_enc', models.CharField(max_length=300, null=True, verbose_name='File enc', blank=True)),
                ('pluritest_file_description', models.TextField(null=True, verbose_name='File description', blank=True)),
                ('pluritest', models.ForeignKey(related_name='pluritest_files', verbose_name='Cell line pluritest', to='celllines.CelllineCharacterizationPluritest')),
            ],
            options={
                'ordering': ['pluritest'],
                'verbose_name': 'Cell line Pluritest file',
                'verbose_name_plural': 'Cell line Pluritest files',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
