# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0012_cellline_primary_disease_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineGenotypingRsNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rs_number', models.CharField(max_length=12, null=True, verbose_name='rs Number', blank=True)),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('allele_carried', models.CharField(max_length=12, null=True, verbose_name='Allele carried through', blank=True)),
                ('cell_line_form', models.CharField(max_length=12, null=True, verbose_name='Is the cell line homozygote or heterozygot for this variant', blank=True)),
                ('cell_line', models.ForeignKey(related_name='rs_number', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line rs number',
                'verbose_name_plural': 'Cell line rs numbers',
            },
        ),
        migrations.CreateModel(
            name='CelllineGenotypingSNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.CharField(max_length=45, null=True, verbose_name='SNP gene name', blank=True)),
                ('chromosomal_position', models.CharField(max_length=45, null=True, verbose_name='SNP choromosomal position', blank=True)),
                ('cell_line', models.ForeignKey(related_name='snps', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line snp',
                'verbose_name_plural': 'Cell line snps',
            },
        ),
        migrations.CreateModel(
            name='CelllineGenotypingVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assembly', models.CharField(max_length=45, null=True, verbose_name='Assembly', blank=True)),
                ('chormosome', models.CharField(max_length=45, null=True, verbose_name='Chormosome', blank=True)),
                ('coordinate', models.CharField(max_length=45, null=True, verbose_name='Coordinate', blank=True)),
                ('reference_allele', models.CharField(max_length=45, null=True, verbose_name='Reference allele', blank=True)),
                ('alternative_allele', models.CharField(max_length=45, null=True, verbose_name='Alternative allele', blank=True)),
                ('protein_sequence_variants', models.CharField(max_length=100, null=True, verbose_name='Protein sequence variants', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genotyping_variant', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genotyping variant',
                'verbose_name_plural': 'Cell line genotyping variants',
            },
        ),
        migrations.RemoveField(
            model_name='celllinesnp',
            name='snpcellline',
        ),
        migrations.RemoveField(
            model_name='celllinesnpdetails',
            name='celllinesnp',
        ),
        migrations.RemoveField(
            model_name='celllinesnprslinks',
            name='celllinesnp',
        ),
        migrations.DeleteModel(
            name='Celllinesnp',
        ),
        migrations.DeleteModel(
            name='Celllinesnpdetails',
        ),
        migrations.DeleteModel(
            name='Celllinesnprslinks',
        ),
    ]
