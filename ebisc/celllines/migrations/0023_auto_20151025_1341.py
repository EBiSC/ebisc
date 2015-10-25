# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0022_auto_20151025_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='culture_medium',
            field=models.CharField(max_length=45, null=True, verbose_name='Culture medium', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='enzymatically',
            field=models.CharField(max_length=45, null=True, verbose_name='Enzymatically', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='enzyme_free',
            field=models.CharField(max_length=45, null=True, verbose_name='Enzyme free', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='passage_method',
            field=models.CharField(max_length=100, null=True, verbose_name='Passage method', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='surface_coating',
            field=models.CharField(max_length=100, null=True, verbose_name='Surface coating', blank=True),
        ),
        migrations.DeleteModel(
            name='CultureMedium',
        ),
        migrations.DeleteModel(
            name='Enzymatically',
        ),
        migrations.DeleteModel(
            name='EnzymeFree',
        ),
        migrations.DeleteModel(
            name='PassageMethod',
        ),
        migrations.DeleteModel(
            name='SurfaceCoating',
        ),
    ]
