# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0017_auto_20151023_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineGenomeAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=45, null=True, verbose_name='Data', blank=True)),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genome_analysis', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genome analysis',
                'verbose_name_plural': 'Cell line genome analysis',
            },
        ),
        migrations.RemoveField(
            model_name='celllinegenomeseq',
            name='genomeseqcellline',
        ),
        migrations.DeleteModel(
            name='Celllinegenomeseq',
        ),
    ]
