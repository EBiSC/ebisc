# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0002_auto_20150623_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineAliquot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamplesid', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('status', models.CharField(max_length=10, verbose_name='Status')),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['biosamplesid'],
                'verbose_name': 'Cell line aliquot',
                'verbose_name_plural': 'Cell line aliquotes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CelllineBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamplesid', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('status', models.CharField(max_length=10, verbose_name='Status')),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['biosamplesid'],
                'verbose_name': 'Cell line batch',
                'verbose_name_plural': 'Cell line batches',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Batchstatus',
        ),
    ]
