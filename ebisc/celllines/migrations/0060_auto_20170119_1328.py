# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0059_cellline_has_diseases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome_location', models.CharField(max_length=500, null=True, verbose_name='Chromosome location', blank=True)),
                ('nucleotide_sequence_hgvs', models.CharField(max_length=1000, null=True, verbose_name='Nucleotide sequence HGSV', blank=True)),
                ('protein_sequence_hgvs', models.CharField(max_length=1000, null=True, verbose_name='Protein sequence HGSV', blank=True)),
                ('zygosity_status', models.CharField(max_length=200, null=True, verbose_name='Zygosity status', blank=True)),
                ('clinvar_id', models.CharField(max_length=200, null=True, verbose_name='ClinVar ID', blank=True)),
                ('dbsnp_id', models.CharField(max_length=200, null=True, verbose_name='dbSNP ID', blank=True)),
                ('dbvar_id', models.CharField(max_length=200, null=True, verbose_name='dbVar ID', blank=True)),
                ('publication_pmid', models.CharField(max_length=200, null=True, verbose_name='PubMed ID', blank=True)),
                ('notes', models.CharField(max_length=1000, null=True, verbose_name='Brief explanation', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
        migrations.RemoveField(
            model_name='celllinedisease',
            name='affected_status',
        ),
        migrations.RemoveField(
            model_name='celllinedisease',
            name='carrier',
        ),
        migrations.RemoveField(
            model_name='celllinedisease',
            name='disease_stage',
        ),
        migrations.CreateModel(
            name='DonorDiseaseVariant',
            fields=[
                ('variant_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.Variant')),
                ('donor_disease', models.ForeignKey(related_name='donor_disease_variants', verbose_name='Donor disease', to='celllines.DonorDisease')),
            ],
            options={
                'ordering': ['donor_disease'],
                'verbose_name': 'Donor disease variant',
                'verbose_name_plural': 'Donor disease variants',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.variant'),
        ),
        migrations.AddField(
            model_name='variant',
            name='gene',
            field=models.ForeignKey(related_name='variant_gene', verbose_name='Gene', blank=True, to='celllines.Molecule', null=True),
        ),
    ]
