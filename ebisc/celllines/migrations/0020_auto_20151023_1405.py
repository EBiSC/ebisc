# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0019_auto_20151023_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelllineGeneticModification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Protocol', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genetic modification',
                'verbose_name_plural': 'Cell line genetic modifications',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationGeneKnockIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_gene_knock_in', verbose_name='Cell line', to='celllines.Cellline')),
                ('target_genes', models.ManyToManyField(related_name='target_genes', to='celllines.Molecule', blank=True)),
                ('transgenes', models.ManyToManyField(related_name='transgenes', to='celllines.Molecule', blank=True)),
                ('transposon', models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True)),
                ('virus', models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Gene knock-in',
                'verbose_name_plural': 'Genetic modifications - Gene knock-in',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationGeneKnockOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_gene_knock_out', verbose_name='Cell line', to='celllines.Cellline')),
                ('target_genes', models.ManyToManyField(to='celllines.Molecule', blank=True)),
                ('transposon', models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True)),
                ('virus', models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Gene knock-out',
                'verbose_name_plural': 'Genetic modifications - Gene knock-out',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationIsogenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_type', models.CharField(max_length=45, null=True, verbose_name='Type of change', blank=True)),
                ('modified_sequence', models.CharField(max_length=100, null=True, verbose_name='Modified sequence', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_isogenic', verbose_name='Cell line', to='celllines.Cellline')),
                ('target_locus', models.ManyToManyField(to='celllines.Molecule', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Isogenic modification',
                'verbose_name_plural': 'Genetic modifications - Isogenic modification',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationTransgeneExpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_transgene_expression', verbose_name='Cell line', to='celllines.Cellline')),
                ('genes', models.ManyToManyField(to='celllines.Molecule', blank=True)),
                ('transposon', models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True)),
                ('virus', models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Transgene Expression',
                'verbose_name_plural': 'Genetic modifications - Transgene Expression',
            },
        ),
        migrations.RemoveField(
            model_name='celllinegenemutations',
            name='genemutationscellline',
        ),
        migrations.RemoveField(
            model_name='celllinegeneticmod',
            name='geneticmodcellline',
        ),
        migrations.RemoveField(
            model_name='celllinegenotypingother',
            name='genometypothercellline',
        ),
        migrations.DeleteModel(
            name='Celllinegenemutations',
        ),
        migrations.DeleteModel(
            name='Celllinegeneticmod',
        ),
        migrations.DeleteModel(
            name='Celllinegenotypingother',
        ),
    ]
