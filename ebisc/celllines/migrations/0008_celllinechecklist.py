# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0007_auto_20150310_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celllinechecklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphologicalassessment', models.BooleanField(default=False, verbose_name='Morphological assessment')),
                ('facs', models.BooleanField(default=False, verbose_name='FACS')),
                ('ihc', models.BooleanField(default=False, verbose_name='IHC')),
                ('pcrforreprofactorremoval', models.BooleanField(default=False, verbose_name='PCR for reprofactor removal')),
                ('pcrforpluripotency', models.BooleanField(default=False, verbose_name='PCR for pluripotency')),
                ('teratoma', models.BooleanField(default=False, verbose_name='Teratoma')),
                ('invitrodifferentiation', models.BooleanField(default=False, verbose_name='Invitro differentiation')),
                ('karyotype', models.BooleanField(default=False, verbose_name='Karyo type')),
                ('cnvanalysis', models.BooleanField(default=False, verbose_name='CNV analysis')),
                ('dnamethylation', models.BooleanField(default=False, verbose_name='DNA methylation')),
                ('microbiologyinclmycoplasma', models.BooleanField(default=False, verbose_name='Micro biology inclmycoplasma')),
                ('dnagenotyping', models.BooleanField(default=False, verbose_name='DNA genotyping')),
                ('hlatyping', models.BooleanField(default=False, verbose_name='HLA typing')),
                ('virustesting', models.BooleanField(default=False, verbose_name='Viru stesting')),
                ('postthawviability', models.BooleanField(default=False, verbose_name='Post thawviability')),
                ('checklistcomments', models.TextField(null=True, verbose_name=b'Checklist comments', blank=True)),
                ('checklistcellline', models.OneToOneField(to='celllines.Cellline')),
            ],
            options={
                'ordering': ['checklistcellline'],
                'verbose_name': 'Cell line checklist',
                'verbose_name_plural': 'Cell line checklists',
            },
            bases=(models.Model,),
        ),
    ]
