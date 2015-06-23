# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0010_auto_20150623_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellLineVectorFreeReprogrammingFactors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.OneToOneField(related_name='vector_free_reprogramming_factors', verbose_name='Cell line', to='celllines.Cellline')),
                ('factor', models.ForeignKey(verbose_name='Vector-free reprogramming factor', blank=True, to='celllines.Vectorfreereprogramfactor', null=True)),
            ],
            options={
                'verbose_name': 'Cell line Vector-free Programming Factor',
                'verbose_name_plural': 'Cell line Vector-free Programming Factors',
            },
        ),
    ]
