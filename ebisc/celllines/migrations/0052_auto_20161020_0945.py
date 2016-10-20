# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0051_auto_20161006_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='passage_number_banked',
            field=models.CharField(max_length=100, null=True, verbose_name='Passage number banked (pre-EBiSC)', blank=True),
        ),
        migrations.AlterField(
            model_name='celllineculturemediumsupplement',
            name='supplement',
            field=models.CharField(max_length=200, verbose_name='Supplement'),
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='reprogramming_passage_number',
            field=models.CharField(max_length=100, null=True, verbose_name='Passage number reprogrammed', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='tissue_procurement_location',
            field=models.CharField(max_length=200, null=True, verbose_name='Location of primary tissue procurement', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinedifferentiationpotency',
            name='passage_number',
            field=models.CharField(max_length=10, verbose_name='Passage number', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='allele_carried',
            field=models.CharField(max_length=200, null=True, verbose_name='Allele carried through', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='alternative_allele',
            field=models.CharField(max_length=200, null=True, verbose_name='Alternative allele', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='assembly',
            field=models.CharField(max_length=200, null=True, verbose_name='Assembly', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='cell_line_form',
            field=models.CharField(max_length=200, null=True, verbose_name='Is the cell line homozygote or heterozygot for this variant', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='chormosome',
            field=models.CharField(max_length=200, null=True, verbose_name='Chormosome', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='coordinate',
            field=models.CharField(max_length=200, null=True, verbose_name='Coordinate', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='protein_sequence_variants',
            field=models.CharField(max_length=300, null=True, verbose_name='Protein sequence variants', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinediseasegenotype',
            name='reference_allele',
            field=models.CharField(max_length=200, null=True, verbose_name='Reference allele', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinegeneticmodification',
            name='types',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=200), null=True, verbose_name='Types of modification', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinegenotypingrsnumber',
            name='rs_number',
            field=models.CharField(max_length=200, null=True, verbose_name='rs Number', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinegenotypingsnp',
            name='chromosomal_position',
            field=models.CharField(max_length=200, null=True, verbose_name='SNP choromosomal position', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinegenotypingsnp',
            name='gene_name',
            field=models.CharField(max_length=200, null=True, verbose_name='SNP gene name', blank=True),
        ),
        migrations.AlterField(
            model_name='celllineintegratingvector',
            name='methods',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=200), null=True, verbose_name='Methods used', blank=True),
        ),
        migrations.AlterField(
            model_name='celllinenonintegratingvector',
            name='methods',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=200), null=True, verbose_name='Methods used', blank=True),
        ),
        migrations.AlterField(
            model_name='celltype',
            name='name',
            field=models.CharField(unique=True, max_length=300, verbose_name='Cell type'),
        ),
        migrations.AlterField(
            model_name='celltype',
            name='purl',
            field=models.URLField(max_length=500, null=True, verbose_name='Purl', blank=True),
        ),
        migrations.AlterField(
            model_name='culturemediumother',
            name='base',
            field=models.CharField(max_length=200, verbose_name='Culture medium base', blank=True),
        ),
        migrations.AlterField(
            model_name='culturemediumother',
            name='protein_source',
            field=models.CharField(max_length=200, null=True, verbose_name='Protein source', blank=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='provider_donor_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, verbose_name='Provider donor ids', size=None),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='allele_carried',
            field=models.CharField(max_length=200, null=True, verbose_name='Allele carried through', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='alternative_allele',
            field=models.CharField(max_length=200, null=True, verbose_name='Alternative allele', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='assembly',
            field=models.CharField(max_length=200, null=True, verbose_name='Assembly', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='chormosome',
            field=models.CharField(max_length=200, null=True, verbose_name='Chormosome', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='coordinate',
            field=models.CharField(max_length=200, null=True, verbose_name='Coordinate', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='homozygous_heterozygous',
            field=models.CharField(max_length=200, null=True, verbose_name='Is the donor homozygous or heterozygous for this variant', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='protein_sequence_variants',
            field=models.CharField(max_length=300, null=True, verbose_name='Protein sequence variants', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotype',
            name='reference_allele',
            field=models.CharField(max_length=200, null=True, verbose_name='Reference allele', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotypingrsnumber',
            name='rs_number',
            field=models.CharField(max_length=200, verbose_name='rs Number'),
        ),
        migrations.AlterField(
            model_name='donorgenotypingsnp',
            name='chromosomal_position',
            field=models.CharField(max_length=200, null=True, verbose_name='SNP choromosomal position', blank=True),
        ),
        migrations.AlterField(
            model_name='donorgenotypingsnp',
            name='gene_name',
            field=models.CharField(max_length=200, verbose_name='SNP gene name'),
        ),
        migrations.AlterField(
            model_name='geneticmodificationgeneknockin',
            name='delivery_method',
            field=models.CharField(max_length=200, null=True, verbose_name='Delivery method', blank=True),
        ),
        migrations.AlterField(
            model_name='geneticmodificationgeneknockout',
            name='delivery_method',
            field=models.CharField(max_length=200, null=True, verbose_name='Delivery method', blank=True),
        ),
        migrations.AlterField(
            model_name='geneticmodificationisogenic',
            name='change_type',
            field=models.CharField(max_length=200, null=True, verbose_name='Type of change', blank=True),
        ),
        migrations.AlterField(
            model_name='geneticmodificationtransgeneexpression',
            name='delivery_method',
            field=models.CharField(max_length=200, null=True, verbose_name='Delivery method', blank=True),
        ),
        migrations.AlterField(
            model_name='germlayer',
            name='germlayer',
            field=models.CharField(max_length=100, verbose_name='Germ layer', blank=True),
        ),
        migrations.AlterField(
            model_name='marker',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Marker', blank=True),
        ),
        migrations.AlterField(
            model_name='morphologymethod',
            name='morphologymethod',
            field=models.CharField(max_length=200, verbose_name='Morphology method', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=500, unique=True, null=True, verbose_name='Organization name', blank=True),
        ),
        migrations.AlterField(
            model_name='vectorfreereprogrammingfactor',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name='Vector free reprogram factor'),
        ),
    ]
