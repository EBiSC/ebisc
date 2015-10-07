# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='phenotype',
        ),
        migrations.AddField(
            model_name='donor',
            name='phenotypes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, verbose_name='Phenotypes', size=None),
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='cell_line',
            field=models.OneToOneField(related_name='derivation', verbose_name='Cell line', to='celllines.Cellline'),
        ),
        migrations.DeleteModel(
            name='Phenotype',
        ),
    ]
