# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0004_auto_20150310_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliquotstatus',
            options={'ordering': [], 'verbose_name': 'Aliquot status', 'verbose_name_plural': 'Aliquot statuses'},
        ),
        migrations.AlterModelOptions(
            name='approveduse',
            options={'ordering': [], 'verbose_name': 'Approved use', 'verbose_name_plural': 'Approved uses'},
        ),
        migrations.AlterModelOptions(
            name='batchstatus',
            options={'ordering': [], 'verbose_name': 'Batch status', 'verbose_name_plural': 'Batch statuses'},
        ),
        migrations.AlterModelOptions(
            name='binnedage',
            options={'ordering': ['id'], 'verbose_name': 'Binned age', 'verbose_name_plural': 'Binned ages'},
        ),
        migrations.AlterModelOptions(
            name='cellline',
            options={'ordering': [], 'verbose_name': 'Cell line', 'verbose_name_plural': 'Cell lines'},
        ),
        migrations.AlterModelOptions(
            name='celllinealiquot',
            options={'ordering': [], 'verbose_name': 'Cell line aliquot', 'verbose_name_plural': 'Cell line aliquotes'},
        ),
        migrations.AlterModelOptions(
            name='celllineannotation',
            options={'ordering': [], 'verbose_name': 'Cell line annotation', 'verbose_name_plural': 'Cell line annotations'},
        ),
        migrations.AlterModelOptions(
            name='celllinebatch',
            options={'ordering': [], 'verbose_name': 'Cell line batch', 'verbose_name_plural': 'Cell line batches'},
        ),
        migrations.AlterModelOptions(
            name='celllinecharacterization',
            options={'ordering': [], 'verbose_name': 'Cell line characterization', 'verbose_name_plural': 'Cell line characterizations'},
        ),
        migrations.AlterModelOptions(
            name='celllinecollection',
            options={'ordering': [], 'verbose_name': 'Cell line collection', 'verbose_name_plural': 'Cell line collections'},
        ),
        migrations.AlterModelOptions(
            name='celllinecomments',
            options={'ordering': [], 'verbose_name': 'Cell line comments', 'verbose_name_plural': 'Cell line comments'},
        ),
        migrations.AlterModelOptions(
            name='celllinecultureconditions',
            options={'ordering': [], 'verbose_name': 'Cell line culture conditions', 'verbose_name_plural': 'Cell line culture conditions'},
        ),
        migrations.AlterModelOptions(
            name='celllineculturesupplements',
            options={'ordering': [], 'verbose_name': 'Cell line culture supplements', 'verbose_name_plural': 'Cell line culture supplements'},
        ),
        migrations.AlterModelOptions(
            name='celllinederivation',
            options={'ordering': [], 'verbose_name': 'Cell line derivation', 'verbose_name_plural': 'Cell line derivations'},
        ),
        migrations.AlterModelOptions(
            name='celllinediffpotency',
            options={'ordering': [], 'verbose_name': 'Cell line diff potency', 'verbose_name_plural': 'Cell line diff potencies'},
        ),
        migrations.AlterModelOptions(
            name='celllinediffpotencymarker',
            options={'ordering': [], 'verbose_name': 'Cell line diff potency marker', 'verbose_name_plural': 'Cell line diff potency markers'},
        ),
        migrations.AlterModelOptions(
            name='celllinediffpotencymolecule',
            options={'ordering': [], 'verbose_name': 'Cell line diff potency molecule', 'verbose_name_plural': 'Cell line diff potency molecules'},
        ),
        migrations.AlterModelOptions(
            name='celllinegenemutations',
            options={'ordering': [], 'verbose_name': 'Cell line gene mutations', 'verbose_name_plural': 'Cell line gene mutations'},
        ),
        migrations.AlterModelOptions(
            name='celllinegenemutationsmolecule',
            options={'ordering': [], 'verbose_name': 'Cell line gene mutations molecule', 'verbose_name_plural': 'Cell line gene mutations molecules'},
        ),
        migrations.AlterModelOptions(
            name='celllinegeneticmod',
            options={'ordering': [], 'verbose_name': 'Cell line genetic mod', 'verbose_name_plural': 'Cell line genetic modes'},
        ),
        migrations.AlterModelOptions(
            name='celllinegenomeseq',
            options={'ordering': [], 'verbose_name': 'Cell line genome seqence', 'verbose_name_plural': 'Cell line genome seqences'},
        ),
        migrations.AlterModelOptions(
            name='celllinegenotypingother',
            options={'ordering': [], 'verbose_name': 'Cell line genotyping other', 'verbose_name_plural': 'Cell line genotyping others'},
        ),
        migrations.AlterModelOptions(
            name='celllinehlatyping',
            options={'ordering': [], 'verbose_name': 'Cell line hla typing', 'verbose_name_plural': 'Cell line hla typing'},
        ),
        migrations.AlterModelOptions(
            name='celllinekaryotype',
            options={'ordering': [], 'verbose_name': 'Cell line karyotype', 'verbose_name_plural': 'Cell line karyotypes'},
        ),
        migrations.AlterModelOptions(
            name='celllinelab',
            options={'ordering': [], 'verbose_name': 'Cell line lab', 'verbose_name_plural': 'Cell line labs'},
        ),
        migrations.AlterModelOptions(
            name='celllinelegal',
            options={'ordering': [], 'verbose_name': 'Cell line legal', 'verbose_name_plural': 'Cell line legal'},
        ),
        migrations.AlterModelOptions(
            name='celllinemarker',
            options={'ordering': [], 'verbose_name': 'Cell line marker', 'verbose_name_plural': 'Cell line markers'},
        ),
        migrations.AlterModelOptions(
            name='celllineorganization',
            options={'ordering': [], 'verbose_name': 'Cell line organization', 'verbose_name_plural': 'Cell line organizations'},
        ),
        migrations.AlterModelOptions(
            name='celllineorgtype',
            options={'ordering': [], 'verbose_name': 'Cell line org type', 'verbose_name_plural': 'Cell line org types'},
        ),
        migrations.AlterModelOptions(
            name='celllinepublication',
            options={'ordering': [], 'verbose_name': 'Cell line publication', 'verbose_name_plural': 'Cell line publications'},
        ),
        migrations.AlterModelOptions(
            name='celllinesnp',
            options={'ordering': [], 'verbose_name': 'Cell line snp', 'verbose_name_plural': 'Cell line snps'},
        ),
        migrations.AlterModelOptions(
            name='celllinesnpdetails',
            options={'ordering': [], 'verbose_name': 'Cell line snp details', 'verbose_name_plural': 'Cell line snp details'},
        ),
        migrations.AlterModelOptions(
            name='celllinesnprslinks',
            options={'ordering': [], 'verbose_name': 'Cell line snp Rs links', 'verbose_name_plural': 'Cell line snp Rs links'},
        ),
        migrations.AlterModelOptions(
            name='celllinestatus',
            options={'ordering': ['celllinestatus'], 'verbose_name': 'Cell line status', 'verbose_name_plural': 'Cell line statuses'},
        ),
        migrations.AlterModelOptions(
            name='celllinestrfingerprinting',
            options={'ordering': [], 'verbose_name': 'Cell line str finger printing', 'verbose_name_plural': 'Cell line str finger printings'},
        ),
        migrations.AlterModelOptions(
            name='celllinevalue',
            options={'ordering': [], 'verbose_name': 'Cell line value', 'verbose_name_plural': 'Cell line values'},
        ),
        migrations.AlterModelOptions(
            name='celllinevector',
            options={'ordering': [], 'verbose_name': 'Cell line vector', 'verbose_name_plural': 'Cell line vectors'},
        ),
        migrations.AlterModelOptions(
            name='celllinevectorfreereprogramming',
            options={'ordering': [], 'verbose_name': 'Cell line vector free reprogramming', 'verbose_name_plural': 'Cell line vector free reprogrammings'},
        ),
        migrations.AlterModelOptions(
            name='celllinevectormolecule',
            options={'ordering': [], 'verbose_name': 'Cell line vector molecule', 'verbose_name_plural': 'Cell line vector molecules'},
        ),
        migrations.AlterModelOptions(
            name='celltype',
            options={'ordering': [], 'verbose_name': 'Cell type', 'verbose_name_plural': 'Cell types'},
        ),
        migrations.AlterModelOptions(
            name='clinicaltreatmentb4donation',
            options={'ordering': [], 'verbose_name': 'Clininical treatment b4 donation', 'verbose_name_plural': 'Clininical treatment b4 donations'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': [], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'ordering': [], 'verbose_name': 'Contact type', 'verbose_name_plural': 'Contact types'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': [], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='culturemedium',
            options={'ordering': [], 'verbose_name': 'Culture medium', 'verbose_name_plural': 'Culture mediums'},
        ),
        migrations.AlterModelOptions(
            name='culturesystem',
            options={'ordering': [], 'verbose_name': 'Culture system', 'verbose_name_plural': 'Culture systems'},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['disease'], 'verbose_name': 'Disease', 'verbose_name_plural': 'Diseases'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': [], 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'ordering': [], 'verbose_name': 'Document type', 'verbose_name_plural': 'Document types'},
        ),
        migrations.AlterModelOptions(
            name='donor',
            options={'ordering': [], 'verbose_name': 'Donor', 'verbose_name_plural': 'Donors'},
        ),
        migrations.AlterModelOptions(
            name='ebisckeyword',
            options={'ordering': [], 'verbose_name': 'Ebisc keyword', 'verbose_name_plural': 'Ebisc keywords'},
        ),
        migrations.AlterModelOptions(
            name='enzymatically',
            options={'ordering': [], 'verbose_name': 'Enzymatically', 'verbose_name_plural': 'Enzymatically'},
        ),
        migrations.AlterModelOptions(
            name='enzymefree',
            options={'ordering': [], 'verbose_name': 'Enzyme free', 'verbose_name_plural': 'Enzyme free'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': [], 'verbose_name': 'Gender', 'verbose_name_plural': 'Genders'},
        ),
        migrations.AlterModelOptions(
            name='germlayer',
            options={'ordering': [], 'verbose_name': 'Germ layer', 'verbose_name_plural': 'Germ layers'},
        ),
        migrations.AlterModelOptions(
            name='hla',
            options={'ordering': [], 'verbose_name': 'Hla', 'verbose_name_plural': 'Hla'},
        ),
        migrations.AlterModelOptions(
            name='karyotypemethod',
            options={'ordering': [], 'verbose_name': 'Karyotype method', 'verbose_name_plural': 'Karyotype methods'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': [], 'verbose_name': 'Keyword', 'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='lastupdatetype',
            options={'ordering': [], 'verbose_name': 'Last update type', 'verbose_name_plural': 'Last update types'},
        ),
        migrations.AlterModelOptions(
            name='marker',
            options={'ordering': [], 'verbose_name': 'Marker', 'verbose_name_plural': 'Markers'},
        ),
        migrations.AlterModelOptions(
            name='molecule',
            options={'ordering': [], 'verbose_name': 'Molecule', 'verbose_name_plural': 'Molecules'},
        ),
        migrations.AlterModelOptions(
            name='morphologymethod',
            options={'ordering': [], 'verbose_name': 'Morphology method', 'verbose_name_plural': 'Morphology methods'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': [], 'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterModelOptions(
            name='orgtype',
            options={'ordering': [], 'verbose_name': 'Organization type', 'verbose_name_plural': 'Organization types'},
        ),
        migrations.AlterModelOptions(
            name='passagemethod',
            options={'ordering': [], 'verbose_name': 'Passage method', 'verbose_name_plural': 'Passage methods'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': [], 'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='phenotype',
            options={'ordering': [], 'verbose_name': 'Phenotype', 'verbose_name_plural': 'Phenotypes'},
        ),
        migrations.AlterModelOptions(
            name='phonecountrycode',
            options={'ordering': [], 'verbose_name': 'Phone country code', 'verbose_name_plural': 'Phone country codes'},
        ),
        migrations.AlterModelOptions(
            name='postcode',
            options={'ordering': [], 'verbose_name': 'Postcode', 'verbose_name_plural': 'Postcodes'},
        ),
        migrations.AlterModelOptions(
            name='primarycelldevelopmentalstage',
            options={'ordering': [], 'verbose_name': 'Primary cell developmental stage', 'verbose_name_plural': 'Primary cell developmental stages'},
        ),
        migrations.AlterModelOptions(
            name='proteinsource',
            options={'ordering': [], 'verbose_name': 'Protein source', 'verbose_name_plural': 'Protein sources'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': [], 'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod1',
            options={'ordering': [], 'verbose_name': 'Reprogramming method 1', 'verbose_name_plural': 'Reprogramming methods 1'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod2',
            options={'ordering': [], 'verbose_name': 'Reprogramming method 2', 'verbose_name_plural': 'Reprogramming methods 2'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod3',
            options={'ordering': [], 'verbose_name': 'Reprogramming method 3', 'verbose_name_plural': 'Reprogramming methods 3'},
        ),
        migrations.AlterModelOptions(
            name='strfplocus',
            options={'ordering': [], 'verbose_name': 'Str fp locus', 'verbose_name_plural': 'Str fp loci'},
        ),
        migrations.AlterModelOptions(
            name='surfacecoating',
            options={'ordering': [], 'verbose_name': 'Surface coating', 'verbose_name_plural': 'Surface coatings'},
        ),
        migrations.AlterModelOptions(
            name='tissuesource',
            options={'ordering': [], 'verbose_name': 'Tissue source', 'verbose_name_plural': 'Tissue sources'},
        ),
        migrations.AlterModelOptions(
            name='transposon',
            options={'ordering': [], 'verbose_name': 'Transposon', 'verbose_name_plural': 'Transposons'},
        ),
        migrations.AlterModelOptions(
            name='units',
            options={'ordering': [], 'verbose_name': 'Units', 'verbose_name_plural': 'Units'},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'ordering': [], 'verbose_name': 'User account', 'verbose_name_plural': 'User accounts'},
        ),
        migrations.AlterModelOptions(
            name='useraccounttype',
            options={'ordering': [], 'verbose_name': 'User account type', 'verbose_name_plural': 'User account types'},
        ),
        migrations.AlterModelOptions(
            name='vector',
            options={'ordering': [], 'verbose_name': 'Vector', 'verbose_name_plural': 'Vectors'},
        ),
        migrations.AlterModelOptions(
            name='vectorfreereprogramfactor',
            options={'ordering': [], 'verbose_name': 'Vector free reprogram factor', 'verbose_name_plural': 'Vector free reprogram factors'},
        ),
        migrations.AlterModelOptions(
            name='vectortype',
            options={'ordering': [], 'verbose_name': 'Vector type', 'verbose_name_plural': 'Vector types'},
        ),
        migrations.AlterModelOptions(
            name='virus',
            options={'ordering': [], 'verbose_name': 'Virus', 'verbose_name_plural': 'Viruses'},
        ),
        migrations.AlterField(
            model_name='accesslevel',
            name='accesslevel',
            field=models.CharField(max_length=20, verbose_name='Access level', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aliquotstatus',
            name='aliquotstatus',
            field=models.CharField(max_length=20, verbose_name='Aliquot status', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='approveduse',
            name='approveduse',
            field=models.CharField(max_length=60, verbose_name='Approved use', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='batchstatus',
            name='batchstatus',
            field=models.CharField(max_length=20, verbose_name='Batch status', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='binnedage',
            name='binnedage',
            field=models.CharField(max_length=5, verbose_name='Binned age', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='biosamplesid',
            field=models.CharField(unique=True, max_length=12, verbose_name='Biosamples id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinecomments',
            field=models.TextField(null=True, verbose_name='Cell line comments', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinediseaseaddinfo',
            field=models.CharField(max_length=100, verbose_name='Cell line disease add info', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllineecaccurl',
            field=models.URLField(null=True, verbose_name='Cell line ecacc url', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinename',
            field=models.CharField(unique=True, max_length=15, verbose_name='Cell line name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinenamesynonyms',
            field=models.TextField(null=True, verbose_name='Cell line name synonyms', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='depositorscelllineuri',
            field=models.CharField(max_length=45, verbose_name='Depositors cell line uri', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinealiquot',
            name='aliquotstatusdate',
            field=models.CharField(max_length=20, verbose_name='Aliquot status date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineannotation',
            name='celllineannotation',
            field=models.TextField(null=True, verbose_name='Cell line annotation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineannotation',
            name='celllineannotationsource',
            field=models.CharField(max_length=45, verbose_name='Cell line annotation source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineannotation',
            name='celllineannotationsourceid',
            field=models.CharField(max_length=45, verbose_name='Cell line annotation source id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineannotation',
            name='celllineannotationsourceversion',
            field=models.CharField(max_length=45, verbose_name='Cell line annotation source version', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinebatch',
            name='batchstatusdate',
            field=models.CharField(max_length=20, verbose_name='Batch status date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='certificateofanalysispassage',
            field=models.CharField(max_length=5, verbose_name='Certificate of analysis passage', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='hepititusb',
            field=models.IntegerField(null=True, verbose_name='Hepititus b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='hepititusc',
            field=models.IntegerField(null=True, verbose_name='Hepititus c', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='hiv1screening',
            field=models.IntegerField(null=True, verbose_name='Hiv1 screening', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecharacterization',
            name='hiv2screening',
            field=models.IntegerField(null=True, verbose_name='Hiv2 screening', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecollection',
            name='celllinecollectiontotal',
            field=models.IntegerField(null=True, verbose_name='Cell line collection total', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecollection',
            name='celllinecollectionupdatedby',
            field=models.CharField(max_length=45, verbose_name='Cell line collection updated by', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecollection',
            name='celllinecollectionupdatetype',
            field=models.IntegerField(null=True, verbose_name='Cell line collection update type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecomments',
            name='celllinecommentsupdatedby',
            field=models.IntegerField(null=True, verbose_name='Cell line comments updated by', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecomments',
            name='celllinecommentsupdatedtype',
            field=models.IntegerField(null=True, verbose_name='Cell line comments updated type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecomments',
            name='commentscellline',
            field=models.IntegerField(null=True, verbose_name='Comments cell line', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='co2concentration',
            field=models.IntegerField(null=True, verbose_name='Co2 concentration', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='feedercellid',
            field=models.CharField(max_length=45, verbose_name='Feeder cell id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='feedercelltype',
            field=models.CharField(max_length=45, verbose_name='Feeder cell type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinecultureconditions',
            name='o2concentration',
            field=models.IntegerField(null=True, verbose_name='O2 concentration', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineculturesupplements',
            name='supplementamount',
            field=models.CharField(max_length=45, verbose_name='Supplement amount', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='availableasclinicalgrade',
            field=models.CharField(max_length=4, verbose_name='Available as clinical grade', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='derivedundergmp',
            field=models.CharField(max_length=4, verbose_name='Derived under gmp', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='primarycelltypecellfinderid',
            field=models.CharField(max_length=45, verbose_name='Primary cell type cell finder id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='primarycelltypename',
            field=models.CharField(max_length=45, verbose_name='Primary cell type name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='selectioncriteriaforclones',
            field=models.TextField(null=True, verbose_name='Selection criteria for clones', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='xenofreeconditions',
            field=models.CharField(max_length=4, verbose_name='Xeno free conditions', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinediffpotency',
            name='passagenumber',
            field=models.CharField(max_length=5, verbose_name='Passage number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinediffpotencymolecule',
            name='celllinediffpotencymarker',
            field=models.IntegerField(null=True, verbose_name='Cell line diff potency marker', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinegeneticmod',
            name='celllinegeneticmod',
            field=models.CharField(max_length=45, verbose_name='Cell line genetic mod', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinegenomeseq',
            name='celllinegenomeseqlink',
            field=models.CharField(max_length=45, verbose_name='Cell line genome seq link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinegenotypingother',
            name='celllinegenotypingother',
            field=models.TextField(null=True, verbose_name='Cell line geno typing other', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinehlatyping',
            name='celllinehlaallele1',
            field=models.CharField(max_length=45, verbose_name='Cell line hla all ele1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinehlatyping',
            name='celllinehlaallele2',
            field=models.CharField(max_length=45, verbose_name='Cell line hla all ele2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinehlatyping',
            name='celllinehlaclass',
            field=models.IntegerField(null=True, verbose_name='Cell line hla class', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinekaryotype',
            name='passagenumber',
            field=models.CharField(max_length=5, verbose_name='Passage number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelab',
            name='clonenumber',
            field=models.IntegerField(null=True, verbose_name='Clone number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelab',
            name='culturesystemcomment',
            field=models.CharField(max_length=45, verbose_name='Culture system comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelab',
            name='expansioninprogress',
            field=models.IntegerField(null=True, verbose_name='Expansion in progress', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelab',
            name='passagenumber',
            field=models.CharField(max_length=5, verbose_name='Passage number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q10managedaccess',
            field=models.TextField(null=True, verbose_name='Q10 managed access', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q1donorconsent',
            field=models.IntegerField(null=True, verbose_name='Q1 donor consent', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q2donortrace',
            field=models.IntegerField(null=True, verbose_name='Q2 donor trace', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q3irbapproval',
            field=models.IntegerField(null=True, verbose_name='Q3 irb approval', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q5informedconsentreference',
            field=models.CharField(max_length=20, verbose_name='Q5 informed consent reference', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q6restrictions',
            field=models.TextField(null=True, verbose_name='Q6 restrictions', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q7iprestrictions',
            field=models.TextField(null=True, verbose_name='Q7 ip restrictions', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q9applicablelegislationandregulation',
            field=models.TextField(null=True, verbose_name='Q9 applicable legislation and regulation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineorganization',
            name='orgstatus',
            field=models.IntegerField(null=True, verbose_name='Org status', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineorgtype',
            name='celllineorgtype',
            field=models.CharField(max_length=45, verbose_name='Cell line org type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinepublication',
            name='celllinepublicationdoiurl',
            field=models.URLField(null=True, verbose_name='Cell line publication doi url', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinepublication',
            name='pubmedreference',
            field=models.CharField(max_length=45, verbose_name='Pubmed reference', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinesnpdetails',
            name='celllinesnpchromosomalposition',
            field=models.CharField(max_length=45, verbose_name='Cell line snp chromosomal position', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinesnpdetails',
            name='celllinesnpgene',
            field=models.CharField(max_length=45, verbose_name='Cell line snp gene', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinesnprslinks',
            name='rslink',
            field=models.CharField(max_length=100, verbose_name='Rs link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinesnprslinks',
            name='rsnumber',
            field=models.CharField(max_length=45, verbose_name='Rs number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinestatus',
            name='celllinestatus',
            field=models.CharField(max_length=50, verbose_name='Cell line status', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinestrfingerprinting',
            name='allele1',
            field=models.CharField(max_length=45, verbose_name='All ele1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinestrfingerprinting',
            name='allele2',
            field=models.CharField(max_length=45, verbose_name='All ele2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevalue',
            name='othervalue',
            field=models.CharField(max_length=100, verbose_name='Other value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevalue',
            name='potentialuse',
            field=models.CharField(max_length=100, verbose_name='Potential use', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevalue',
            name='valuetoresearch',
            field=models.CharField(max_length=100, verbose_name='Value to research', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevalue',
            name='valuetosociety',
            field=models.CharField(max_length=100, verbose_name='Value to society', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinevector',
            name='vectorexcisable',
            field=models.CharField(max_length=4, verbose_name='Vector excisable', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celltype',
            name='celltype',
            field=models.CharField(max_length=30, verbose_name='Celltypes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clinicaltreatmentb4donation',
            name='clininicaltreatmentb4donation',
            field=models.CharField(max_length=45, verbose_name='Clininical treatment b4 donation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='buildingnumber',
            field=models.CharField(max_length=20, verbose_name='Building number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='emailaddress',
            field=models.CharField(max_length=45, verbose_name='Email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobilephone',
            field=models.CharField(max_length=20, verbose_name='Mobile phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='officephone',
            field=models.CharField(max_length=20, verbose_name='Office phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='statecounty',
            field=models.IntegerField(null=True, verbose_name='State county', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='suiteoraptordept',
            field=models.CharField(max_length=10, verbose_name='Suite or apt or dept', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacttype',
            name='contacttype',
            field=models.CharField(max_length=45, verbose_name='Contact type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='countrycode',
            field=models.CharField(max_length=3, verbose_name='Country code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='culturemedium',
            name='culturemediumbase',
            field=models.CharField(max_length=45, verbose_name='Culture medium base', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='culturemedium',
            name='serumconcentration',
            field=models.IntegerField(null=True, verbose_name='Serum concentration', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='culturesystem',
            name='culturesystem',
            field=models.CharField(max_length=45, verbose_name='Culture system', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disease',
            name='icdcode',
            field=models.CharField(max_length=10, unique=True, null=True, verbose_name='ICD code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='accesslevel',
            field=models.IntegerField(null=True, verbose_name='Access level', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='cellline',
            field=models.IntegerField(null=True, verbose_name='Cell line', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='documentdepositor',
            field=models.IntegerField(null=True, verbose_name='Document depositor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='documentupdate',
            field=models.IntegerField(null=True, verbose_name='Document update', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='documentupdatedby',
            field=models.IntegerField(null=True, verbose_name='Document updated by', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='documentupdatetype',
            field=models.IntegerField(null=True, verbose_name='Document update type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='documenttype',
            field=models.CharField(max_length=30, verbose_name='Document type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='cellabnormalkaryotype',
            field=models.CharField(max_length=45, verbose_name='Cell abnormal karyotype', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='diseaseadditionalinfo',
            field=models.CharField(max_length=45, verbose_name='Disease additional info', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='donorabnormalkaryotype',
            field=models.CharField(max_length=45, verbose_name='Donor abnormal karyotype', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='hescregdonorid',
            field=models.CharField(max_length=3, verbose_name='Hescreg donor id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='otherclinicalinformation',
            field=models.CharField(max_length=100, verbose_name='Other clinical information', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donor',
            name='providerdonorid',
            field=models.CharField(max_length=45, verbose_name='Provider donor id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enzymefree',
            name='enzymefree',
            field=models.CharField(max_length=45, verbose_name='Enzyme free', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='germlayer',
            name='germlayer',
            field=models.CharField(max_length=15, verbose_name='Germ layer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='karyotypemethod',
            name='karyotypemethod',
            field=models.CharField(max_length=45, verbose_name='Karyotype method', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lastupdatetype',
            name='lastupdatetype',
            field=models.CharField(max_length=45, verbose_name='Last update type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='molecule',
            name='moleculename',
            field=models.CharField(max_length=45, verbose_name='Molecule name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='molecule',
            name='referencesource',
            field=models.CharField(max_length=45, verbose_name='Reference source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='molecule',
            name='referencesourceid',
            field=models.CharField(max_length=45, verbose_name='Reference source id', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='morphologymethod',
            name='morphologymethod',
            field=models.CharField(max_length=45, verbose_name='Morphology method', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizationname',
            field=models.CharField(max_length=45, verbose_name='Organization name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizationshortname',
            field=models.CharField(unique=True, max_length=6, verbose_name='Organization short name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orgtype',
            name='orgtype',
            field=models.CharField(max_length=45, verbose_name='Org type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='passagemethod',
            name='passagemethod',
            field=models.CharField(max_length=45, verbose_name='Passage method', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='personfirstname',
            field=models.CharField(max_length=45, verbose_name='Person first name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='personlastname',
            field=models.CharField(max_length=20, verbose_name='Person last name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarycelldevelopmentalstage',
            name='primarycelldevelopmentalstage',
            field=models.CharField(max_length=20, verbose_name='Primary cell developmental stage', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proteinsource',
            name='proteinsource',
            field=models.CharField(max_length=45, verbose_name='Protein source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reprogrammingmethod1',
            name='reprogrammingmethod1',
            field=models.CharField(max_length=45, verbose_name='Reprogramming method 1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reprogrammingmethod2',
            name='reprogrammingmethod2',
            field=models.CharField(max_length=45, verbose_name='Reprogramming method 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reprogrammingmethod3',
            name='reprogrammingmethod3',
            field=models.CharField(max_length=45, verbose_name='Reprogramming method 3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='strfplocus',
            name='strfplocus',
            field=models.CharField(max_length=45, verbose_name='Str fp locus', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='surfacecoating',
            name='surfacecoating',
            field=models.CharField(max_length=45, verbose_name='Surface coating', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tissuesource',
            name='tissuesource',
            field=models.CharField(max_length=45, verbose_name='Tissue source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccounttype',
            name='useraccounttype',
            field=models.CharField(max_length=15, verbose_name='User account type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vectorfreereprogramfactor',
            name='vectorfreereprogramfactor',
            field=models.CharField(max_length=15, verbose_name='Vector free reprogram factor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vectortype',
            name='vectortype',
            field=models.CharField(max_length=15, verbose_name='Vector type', blank=True),
            preserve_default=True,
        ),
    ]
