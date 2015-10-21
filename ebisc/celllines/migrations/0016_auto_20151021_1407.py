# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0015_auto_20151021_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinehlatyping',
            options={'ordering': [], 'verbose_name': 'Cell line HLA typing', 'verbose_name_plural': 'Cell line HLA typing'},
        ),
        migrations.RemoveField(
            model_name='celllinehlatyping',
            name='celllinehla',
        ),
        migrations.RemoveField(
            model_name='celllinehlatyping',
            name='celllinehlaallele1',
        ),
        migrations.RemoveField(
            model_name='celllinehlatyping',
            name='celllinehlaallele2',
        ),
        migrations.RemoveField(
            model_name='celllinehlatyping',
            name='celllinehlaclass',
        ),
        migrations.RemoveField(
            model_name='celllinehlatyping',
            name='hlatypingcellline',
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='cell_line',
            field=models.ForeignKey(related_name='hla_typing', default='', verbose_name='Cell line', to='celllines.Cellline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hla',
            field=models.CharField(max_length=10, null=True, verbose_name='HLA', blank=True),
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hla_allele_1',
            field=models.CharField(max_length=45, null=True, verbose_name='Cell line HLA allele 1', blank=True),
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hla_allele_2',
            field=models.CharField(max_length=45, null=True, verbose_name='Cell line HLA allele 2', blank=True),
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hla_class',
            field=models.CharField(max_length=10, null=True, verbose_name='HLA class', blank=True),
        ),
        migrations.DeleteModel(
            name='Hla',
        ),
    ]
