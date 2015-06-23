# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='screening_hepatitis_b',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis b', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='screening_hepatitis_c',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis c', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='screening_hiv1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv1 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='screening_hiv2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv2 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='screening_mycoplasma',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Mycoplasma', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinepublication',
            name='cell_line',
            field=models.ForeignKey(related_name='publications', verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
    ]
