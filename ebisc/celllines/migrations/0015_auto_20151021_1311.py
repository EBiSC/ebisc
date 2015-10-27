# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0014_auto_20151019_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorGenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele_carried', models.CharField(max_length=12, null=True, verbose_name='Allele carried through', blank=True)),
                ('homozygous_heterozygous', models.CharField(max_length=12, null=True, verbose_name='Is the donor homozygous or heterozygous for this variant', blank=True)),
                ('assembly', models.CharField(max_length=45, null=True, verbose_name='Assembly', blank=True)),
                ('chormosome', models.CharField(max_length=45, null=True, verbose_name='Chormosome', blank=True)),
                ('coordinate', models.CharField(max_length=45, null=True, verbose_name='Coordinate', blank=True)),
                ('reference_allele', models.CharField(max_length=45, null=True, verbose_name='Reference allele', blank=True)),
                ('alternative_allele', models.CharField(max_length=45, null=True, verbose_name='Alternative allele', blank=True)),
                ('protein_sequence_variants', models.CharField(max_length=100, null=True, verbose_name='Protein sequence variants', blank=True)),
                ('donor', models.OneToOneField(related_name='donor_genotyping', verbose_name='Donor', to='celllines.Donor')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor Genotyping',
                'verbose_name_plural': 'Donor Genotyping',
            },
        ),
        migrations.CreateModel(
            name='DonorGenotypingRsNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rs_number', models.CharField(max_length=12, verbose_name='rs Number')),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('donor_genotype', models.ForeignKey(related_name='donor_rs_number', verbose_name='Donor Genotype', to='celllines.DonorGenotype')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor rs number',
                'verbose_name_plural': 'Donor rs numbers',
            },
        ),
        migrations.CreateModel(
            name='DonorGenotypingSNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.CharField(max_length=45, verbose_name='SNP gene name')),
                ('chromosomal_position', models.CharField(max_length=45, null=True, verbose_name='SNP choromosomal position', blank=True)),
                ('donor_genotype', models.ForeignKey(related_name='donor_snps', verbose_name='Donor Genotype', to='celllines.DonorGenotype')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor snp',
                'verbose_name_plural': 'Donor snps',
            },
        ),
        migrations.AlterField(
            model_name='celllinegenotypingrsnumber',
            name='disease_genotype',
            field=models.ForeignKey(related_name='rs_number', verbose_name='Cell line disease genotype', blank=True, to='celllines.CelllineDiseaseGenotype', null=True),
        ),
        migrations.AlterField(
            model_name='celllinegenotypingsnp',
            name='disease_genotype',
            field=models.ForeignKey(related_name='snps', verbose_name='Cell line disease genotype', blank=True, to='celllines.CelllineDiseaseGenotype', null=True),
        ),
    ]
