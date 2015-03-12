# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0021_auto_20150312_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='celllineecaccurl',
            field=models.URLField(null=True, verbose_name='Cell line ECACC URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='depositorscelllineuri',
            field=models.CharField(max_length=45, verbose_name='Depositors cell line URI', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='characterizationcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='cultureconditionscellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='derivationcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='legalcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevalue',
            name='valuecellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
    ]
