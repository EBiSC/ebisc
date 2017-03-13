# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0060_auto_20170119_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModificationGeneKnockIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome_location', models.CharField(max_length=500, null=True, verbose_name='Chromosome location - target gene', blank=True)),
                ('chromosome_location_transgene', models.CharField(max_length=500, null=True, verbose_name='Chromosome location - transgene', blank=True)),
                ('delivery_method', models.CharField(max_length=200, null=True, verbose_name='Delivery method', blank=True)),
                ('notes', models.CharField(max_length=1000, null=True, verbose_name='Brief explanation', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-in',
                'verbose_name_plural': 'Genetic modifications - Gene knock-in',
            },
        ),
        migrations.CreateModel(
            name='ModificationGeneKnockOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome_location', models.CharField(max_length=500, null=True, verbose_name='Chromosome location', blank=True)),
                ('delivery_method', models.CharField(max_length=200, null=True, verbose_name='Delivery method', blank=True)),
                ('notes', models.CharField(max_length=1000, null=True, verbose_name='Brief explanation', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-out',
                'verbose_name_plural': 'Genetic modifications - Gene knock-out',
            },
        ),
        migrations.CreateModel(
            name='ModificationIsogenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome_location', models.CharField(max_length=500, null=True, verbose_name='Chromosome location', blank=True)),
                ('nucleotide_sequence_hgvs', models.CharField(max_length=1000, null=True, verbose_name='Nucleotide sequence HGSV', blank=True)),
                ('protein_sequence_hgvs', models.CharField(max_length=1000, null=True, verbose_name='Protein sequence HGSV', blank=True)),
                ('zygosity_status', models.CharField(max_length=200, null=True, verbose_name='Zygosity status', blank=True)),
                ('modification_type', models.CharField(max_length=1000, null=True, verbose_name='Target locus modification type', blank=True)),
                ('notes', models.CharField(max_length=1000, null=True, verbose_name='Brief explanation', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Isogenic modification',
                'verbose_name_plural': 'Genetic modifications - Isogenic modification',
            },
        ),
        migrations.CreateModel(
            name='ModificationTransgeneExpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome_location', models.CharField(max_length=500, null=True, verbose_name='Chromosome location', blank=True)),
                ('delivery_method', models.CharField(max_length=1000, null=True, verbose_name='Delivery method', blank=True)),
                ('notes', models.CharField(max_length=1000, null=True, verbose_name='Brief explanation', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Transgene expression',
                'verbose_name_plural': 'Genetic modifications - Transgene expression',
            },
        ),
        migrations.CreateModel(
            name='ModificationVariantDisease',
            fields=[
                ('variant_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.Variant')),
                ('cellline_disease', models.ForeignKey(related_name='genetic_modification_cellline_disease_variants', verbose_name='Cell line disease', to='celllines.CelllineDisease')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Disease associated variant',
                'verbose_name_plural': 'Genetic modifications - Disease associated variants',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.variant'),
        ),
        migrations.CreateModel(
            name='ModificationVariantNonDisease',
            fields=[
                ('variant_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.Variant')),
                ('cell_line', models.ForeignKey(related_name='genetic_modification_cellline_variants', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Variant non disease',
                'verbose_name_plural': 'Genetic modifications - Variant non disease',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.variant'),
        ),
        migrations.CreateModel(
            name='ModificationGeneKnockInDisease',
            fields=[
                ('modificationgeneknockin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationGeneKnockIn')),
                ('cellline_disease', models.ForeignKey(related_name='genetic_modification_cellline_disease_gene_knock_in', verbose_name='Cell line disease', to='celllines.CelllineDisease')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-in disease related',
                'verbose_name_plural': 'Genetic modifications - Gene knock-in disease related',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationgeneknockin'),
        ),
        migrations.CreateModel(
            name='ModificationGeneKnockInNonDisease',
            fields=[
                ('modificationgeneknockin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationGeneKnockIn')),
                ('cell_line', models.ForeignKey(related_name='genetic_modification_cellline_gene_knock_in', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-in non disease',
                'verbose_name_plural': 'Genetic modifications - Gene knock-in non disease',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationgeneknockin'),
        ),
        migrations.CreateModel(
            name='ModificationGeneKnockOutDisease',
            fields=[
                ('modificationgeneknockout_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationGeneKnockOut')),
                ('cellline_disease', models.ForeignKey(related_name='genetic_modification_cellline_disease_gene_knock_out', verbose_name='Cell line disease', to='celllines.CelllineDisease')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-out disease related',
                'verbose_name_plural': 'Genetic modifications - Gene knock-out disease related',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationgeneknockout'),
        ),
        migrations.CreateModel(
            name='ModificationGeneKnockOutNonDisease',
            fields=[
                ('modificationgeneknockout_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationGeneKnockOut')),
                ('cell_line', models.ForeignKey(related_name='genetic_modification_cellline_gene_knock_out', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Gene knock-out non disease',
                'verbose_name_plural': 'Genetic modifications - Gene knock-out non disease',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationgeneknockout'),
        ),
        migrations.CreateModel(
            name='ModificationIsogenicDisease',
            fields=[
                ('modificationisogenic_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationIsogenic')),
                ('cellline_disease', models.ForeignKey(related_name='genetic_modification_cellline_disease_isogenic', verbose_name='Cell line disease', to='celllines.CelllineDisease')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Isogenic modification disease related',
                'verbose_name_plural': 'Genetic modifications - Isogenic modification disease related',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationisogenic'),
        ),
        migrations.CreateModel(
            name='ModificationIsogenicNonDisease',
            fields=[
                ('modificationisogenic_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationIsogenic')),
                ('cell_line', models.ForeignKey(related_name='genetic_modification_cellline_isogenic', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Isogenic modification non disease',
                'verbose_name_plural': 'Genetic modifications - Isogenic modification non disease',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationisogenic'),
        ),
        migrations.CreateModel(
            name='ModificationTransgeneExpressionDisease',
            fields=[
                ('modificationtransgeneexpression_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationTransgeneExpression')),
                ('cellline_disease', models.ForeignKey(related_name='genetic_modification_cellline_disease_transgene_expression', verbose_name='Cell line disease', to='celllines.CelllineDisease')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Genetic modification - Transgene expression disease related',
                'verbose_name_plural': 'Genetic modifications - Transgene expression disease related',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationtransgeneexpression'),
        ),
        migrations.CreateModel(
            name='ModificationTransgeneExpressionNonDisease',
            fields=[
                ('modificationtransgeneexpression_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='celllines.ModificationTransgeneExpression')),
                ('cell_line', models.ForeignKey(related_name='genetic_modification_cellline_transgene_expression', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['gene'],
                'verbose_name': 'Genetic modification - Transgene expression non disease',
                'verbose_name_plural': 'Genetic modifications - Transgene expression non disease',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, 'celllines.modificationtransgeneexpression'),
        ),
        migrations.AddField(
            model_name='modificationtransgeneexpression',
            name='gene',
            field=models.ForeignKey(related_name='modification_transgene_expression_gene', verbose_name='Gene', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='modificationtransgeneexpression',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='modificationtransgeneexpression',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='modificationisogenic',
            name='gene',
            field=models.ForeignKey(related_name='modification_isogenic_gene', verbose_name='Gene', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockout',
            name='gene',
            field=models.ForeignKey(related_name='modification_gene_knock_out_gene', verbose_name='Gene', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockout',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockout',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockin',
            name='target_gene',
            field=models.ForeignKey(related_name='modification_gene_knock_in_target_gene', verbose_name='Target gene', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockin',
            name='transgene',
            field=models.ForeignKey(related_name='modification_gene_knock_in_transgene', verbose_name='Transgene', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockin',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockin',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
    ]
