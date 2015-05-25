# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0006_auto_20150525_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='name')),
                ('kind', models.CharField(max_length=20, verbose_name='Kind', choices=[(b'gene', 'Gene'), (b'protein', 'Protein')])),
                ('catalog', models.CharField(max_length=20, verbose_name='Gene ID source', choices=[(b'entrez', 'Entrez'), (b'ensembl', 'Ensembl')])),
                ('catalog_id', models.CharField(max_length=20, verbose_name='ID')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Gene',
                'verbose_name_plural': 'Genes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='gene',
            unique_together=set([('catalog', 'catalog_id')]),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Gene', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Gene', null=True, blank=True),
            preserve_default=True,
        ),
    ]
