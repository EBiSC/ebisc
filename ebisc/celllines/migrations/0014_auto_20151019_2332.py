# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0013_auto_20151019_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineDiseaseGenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele_carried', models.CharField(max_length=12, null=True, verbose_name='Allele carried through', blank=True)),
                ('cell_line_form', models.CharField(max_length=12, null=True, verbose_name='Is the cell line homozygote or heterozygot for this variant', blank=True)),
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
                'verbose_name': 'Cell line disease associated genotype',
                'verbose_name_plural': 'Cell line disease associated genotypes',
            },
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingvariant',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingrsnumber',
            name='allele_carried',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingrsnumber',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingrsnumber',
            name='cell_line_form',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingsnp',
            name='cell_line',
        ),
        migrations.DeleteModel(
            name='CelllineGenotypingVariant',
        ),
        migrations.AddField(
            model_name='celllinegenotypingrsnumber',
            name='disease_genotype',
            field=models.ForeignKey(related_name='rs_number', verbose_name='Cell line', blank=True, to='celllines.CelllineDiseaseGenotype', null=True),
        ),
        migrations.AddField(
            model_name='celllinegenotypingsnp',
            name='disease_genotype',
            field=models.ForeignKey(related_name='snps', verbose_name='Cell line', blank=True, to='celllines.CelllineDiseaseGenotype', null=True),
        ),
    ]
