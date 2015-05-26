# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0008_auto_20150525_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinecharacterization',
            options={'ordering': ['cell_line'], 'verbose_name': 'Cell line characterization', 'verbose_name_plural': 'Cell line characterizations'},
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='certificateofanalysispassage',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='characterizationcellline',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='hepititusb',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='hepititusc',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='hiv1screening',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='hiv2screening',
        ),
        migrations.RemoveField(
            model_name='celllinecharacterization',
            name='mycoplasma',
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='cell_line',
            field=models.OneToOneField(default=0, verbose_name='Cell line', to='celllines.Cellline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='certificate_of_analysis_passage_number',
            field=models.IntegerField(max_length=5, null=True, verbose_name='Certificate of analysis passage', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='screening_hepatitis_b',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis b', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='screening_hepatitis_c',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis c', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='screening_hiv1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv1 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='screening_hiv2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv2 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='screening_mycoplasma',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Mycoplasma', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')]),
            preserve_default=True,
        ),
    ]
