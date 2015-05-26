# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoleculeReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog', models.CharField(max_length=20, verbose_name='Molecule ID source', choices=[(b'entrez', 'Entrez'), (b'ensembl', 'Ensembl')])),
                ('catalog_id', models.CharField(max_length=20, verbose_name='ID')),
                ('molecule', models.ForeignKey(verbose_name=b'Molecule', to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule', 'catalog'],
                'verbose_name': 'Molecule reference',
                'verbose_name_plural': 'Molecule references',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='moleculereference',
            unique_together=set([('molecule', 'catalog')]),
        ),
        migrations.AlterModelOptions(
            name='molecule',
            options={'ordering': ['name', 'kind'], 'verbose_name': 'Molecule', 'verbose_name_plural': 'Molecules'},
        ),
        migrations.AlterUniqueTogether(
            name='molecule',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='molecule',
            name='catalog_id',
        ),
        migrations.RemoveField(
            model_name='molecule',
            name='catalog',
        ),
    ]
