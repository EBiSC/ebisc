# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0016_auto_20151021_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinestrfingerprinting',
            options={'ordering': [], 'verbose_name': 'Cell line STR finger printing', 'verbose_name_plural': 'Cell line STR finger printing'},
        ),
        migrations.RemoveField(
            model_name='celllinestrfingerprinting',
            name='strfpcellline',
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='cell_line',
            field=models.ForeignKey(related_name='str_fingerprinting', default='', verbose_name='Cell line', to='celllines.Cellline'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='celllinestrfingerprinting',
            name='allele1',
            field=models.CharField(max_length=45, null=True, verbose_name='Allele 1', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinestrfingerprinting',
            name='allele2',
            field=models.CharField(max_length=45, null=True, verbose_name='Allele 2', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinestrfingerprinting',
            name='locus',
            field=models.CharField(max_length=45, null=True, verbose_name='Locus', blank=True),
        ),
        migrations.DeleteModel(
            name='Strfplocus',
        ),
    ]
