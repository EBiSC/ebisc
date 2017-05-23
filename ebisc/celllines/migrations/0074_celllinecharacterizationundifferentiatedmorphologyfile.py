# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0073_celllinecharacterizationepipluriscorefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineCharacterizationUndifferentiatedMorphologyFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphology_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='File', blank=True)),
                ('morphology_file_enc', models.CharField(max_length=300, null=True, verbose_name='File enc', blank=True)),
                ('morphology_file_description', models.TextField(null=True, verbose_name='File description', blank=True)),
                ('cell_line', models.ForeignKey(related_name='undifferentiated_morphology_files', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line undifferentiated cells morphology file',
                'verbose_name_plural': 'Cell line undifferentiated cells morphology files',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
