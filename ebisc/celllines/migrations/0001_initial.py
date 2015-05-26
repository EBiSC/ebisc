# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='Age range')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Age range',
                'verbose_name_plural': 'Age ranges',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApprovedUse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Approved use', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Approved use',
                'verbose_name_plural': 'Approved uses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Batchstatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batchstatus', models.CharField(max_length=20, verbose_name='Batch status', blank=True)),
            ],
            options={
                'ordering': ['batchstatus'],
                'verbose_name': 'Batch status',
                'verbose_name_plural': 'Batch statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cellline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllineaccepted', models.CharField(default=b'pending', max_length=10, verbose_name='Cell line accepted', choices=[(b'pending', 'Pending'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')])),
                ('biosamplesid', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('celllinename', models.CharField(unique=True, max_length=15, verbose_name='Cell line name')),
                ('celllinediseaseaddinfo', models.CharField(max_length=100, null=True, verbose_name='Cell line disease info', blank=True)),
                ('celllinetissuedate', models.DateField(null=True, verbose_name='Cell line tissue date', blank=True)),
                ('celllinenamesynonyms', models.CharField(max_length=500, null=True, verbose_name='Cell line name synonyms', blank=True)),
                ('depositorscelllineuri', models.CharField(max_length=45, verbose_name='Depositors cell line URI', blank=True)),
                ('celllinecomments', models.TextField(null=True, verbose_name='Cell line comments', blank=True)),
                ('celllineecaccurl', models.URLField(null=True, verbose_name='Cell line ECACC URL', blank=True)),
            ],
            options={
                'ordering': ['biosamplesid'],
                'verbose_name': 'Cell line',
                'verbose_name_plural': 'Cell lines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineCharacterization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificate_of_analysis_passage_number', models.CharField(max_length=10, null=True, verbose_name='Certificate of analysis passage number', blank=True)),
                ('screening_hiv1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv1 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')])),
                ('screening_hiv2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv2 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')])),
                ('screening_hepatitis_b', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis b', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')])),
                ('screening_hepatitis_c', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis c', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')])),
                ('screening_mycoplasma', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mycoplasma', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not-done', 'Not done')])),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line characterization',
                'verbose_name_plural': 'Cell line characterizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinechecklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphologicalassessment', models.BooleanField(default=False, verbose_name='Morphological assessment')),
                ('facs', models.BooleanField(default=False, verbose_name='FACS')),
                ('ihc', models.BooleanField(default=False, verbose_name='IHC')),
                ('pcrforreprofactorremoval', models.BooleanField(default=False, verbose_name='PCR for reprofactor removal')),
                ('pcrforpluripotency', models.BooleanField(default=False, verbose_name='PCR for pluripotency')),
                ('teratoma', models.BooleanField(default=False, verbose_name='Teratoma')),
                ('invitrodifferentiation', models.BooleanField(default=False, verbose_name='Invitro differentiation')),
                ('karyotype', models.BooleanField(default=False, verbose_name='Karyo type')),
                ('cnvanalysis', models.BooleanField(default=False, verbose_name='CNV analysis')),
                ('dnamethylation', models.BooleanField(default=False, verbose_name='DNA methylation')),
                ('microbiologyinclmycoplasma', models.BooleanField(default=False, verbose_name='Micro biology inclmycoplasma')),
                ('dnagenotyping', models.BooleanField(default=False, verbose_name='DNA genotyping')),
                ('hlatyping', models.BooleanField(default=False, verbose_name='HLA typing')),
                ('virustesting', models.BooleanField(default=False, verbose_name='Virus testing')),
                ('postthawviability', models.BooleanField(default=False, verbose_name='Post thawviability')),
                ('checklistcomments', models.TextField(null=True, verbose_name=b'Checklist comments', blank=True)),
                ('checklistcellline', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['checklistcellline'],
                'verbose_name': 'Cell line checklist',
                'verbose_name_plural': 'Cell line checklists',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinecollectiontotal', models.IntegerField(null=True, verbose_name='Cell line collection total', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Cell line collection',
                'verbose_name_plural': 'Cell line collections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecomments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commentscellline', models.IntegerField(null=True, verbose_name='Comments cell line', blank=True)),
                ('celllinecomments', models.TextField(blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line comments',
                'verbose_name_plural': 'Cell line comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecultureconditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedercelltype', models.CharField(max_length=45, null=True, verbose_name='Feeder cell type', blank=True)),
                ('feedercellid', models.CharField(max_length=45, null=True, verbose_name='Feeder cell id', blank=True)),
                ('o2concentration', models.IntegerField(null=True, verbose_name='O2 concentration', blank=True)),
                ('co2concentration', models.IntegerField(null=True, verbose_name='Co2 concentration', blank=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line culture conditions',
                'verbose_name_plural': 'Cell line culture conditions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineCultureMediumSupplement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplement', models.CharField(max_length=45, verbose_name='Supplement')),
                ('amount', models.CharField(max_length=45, null=True, verbose_name='Amount', blank=True)),
                ('cell_line_culture_conditions', models.ForeignKey(related_name='medium_supplements', verbose_name='Cell line culture conditions', to='celllines.Celllinecultureconditions')),
            ],
            options={
                'ordering': ['supplement'],
                'verbose_name': 'Cell line culture supplements',
                'verbose_name_plural': 'Cell line culture supplements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinederivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primarycelltypename', models.CharField(max_length=45, verbose_name='Primary cell type name', blank=True)),
                ('primarycelltypecellfinderid', models.CharField(max_length=45, verbose_name='Primary cell type cell finder id', blank=True)),
                ('selectioncriteriaforclones', models.TextField(null=True, verbose_name='Selection criteria for clones', blank=True)),
                ('xenofreeconditions', models.NullBooleanField(default=None, verbose_name='Xeno free conditions')),
                ('derivedundergmp', models.NullBooleanField(default=None, verbose_name='Derived under gmp')),
                ('availableasclinicalgrade', models.CharField(max_length=4, verbose_name='Available as clinical grade', blank=True)),
                ('cell_line', models.OneToOneField(null=True, blank=True, to='celllines.Cellline', verbose_name='Cell line')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line derivation',
                'verbose_name_plural': 'Cell line derivations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenemutations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblink', models.CharField(max_length=100, verbose_name='Weblink', blank=True)),
                ('genemutationscellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line gene mutations',
                'verbose_name_plural': 'Cell line gene mutations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegeneticmod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegeneticmod', models.CharField(max_length=45, verbose_name='Cell line genetic mod', blank=True)),
                ('geneticmodcellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genetic mod',
                'verbose_name_plural': 'Cell line genetic modes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenomeseq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegenomeseqlink', models.CharField(max_length=45, verbose_name='Cell line genome seq link', blank=True)),
                ('genomeseqcellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genome seqence',
                'verbose_name_plural': 'Cell line genome seqences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenotypingother',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegenotypingother', models.TextField(null=True, verbose_name='Cell line geno typing other', blank=True)),
                ('genometypothercellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genotyping other',
                'verbose_name_plural': 'Cell line genotyping others',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinehlatyping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinehlaclass', models.IntegerField(null=True, verbose_name='Cell line hla class', blank=True)),
                ('celllinehlaallele1', models.CharField(max_length=45, verbose_name='Cell line hla all ele1', blank=True)),
                ('celllinehlaallele2', models.CharField(max_length=45, verbose_name='Cell line hla all ele2', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line hla typing',
                'verbose_name_plural': 'Cell line hla typing',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excisable', models.NullBooleanField(default=None, verbose_name='Excisable')),
                ('cell_line', models.OneToOneField(related_name='integrating_vector', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line integrating vector',
                'verbose_name_plural': 'Cell line integrating vectors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineKaryotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karyotype', models.CharField(max_length=500, null=True, verbose_name='Karyotype', blank=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='karyotype', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line karyotype',
                'verbose_name_plural': 'Cell line karyotypes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinelab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cryodate', models.DateField(null=True, blank=True)),
                ('expansioninprogress', models.IntegerField(null=True, verbose_name='Expansion in progress', blank=True)),
                ('funder', models.CharField(max_length=45, verbose_name='Funder', blank=True)),
                ('mutagene', models.CharField(max_length=100, verbose_name='Mutagene', blank=True)),
                ('clonenumber', models.IntegerField(null=True, verbose_name='Clone number', blank=True)),
                ('passagenumber', models.CharField(max_length=5, verbose_name='Passage number', blank=True)),
                ('culturesystemcomment', models.CharField(max_length=45, verbose_name='Culture system comment', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line lab',
                'verbose_name_plural': 'Cell line labs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineLegal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('donor_consent', models.NullBooleanField(default=None, verbose_name='Donor consent')),
                ('donor_trace', models.IntegerField(null=True, verbose_name='Donor trace', blank=True)),
                ('irb_approval', models.IntegerField(null=True, verbose_name='IRB approval', blank=True)),
                ('informed_consent_reference', models.CharField(max_length=20, verbose_name='Informed consent reference', blank=True)),
                ('restrictions', models.TextField(null=True, verbose_name='Restrictions', blank=True)),
                ('ip_restrictions', models.TextField(null=True, verbose_name='IP restrictions', blank=True)),
                ('applicable_legislation_and_regulation', models.TextField(null=True, verbose_name='Applicable legislation and regulation', blank=True)),
                ('managed_access', models.TextField(null=True, verbose_name='Managed access', blank=True)),
                ('approved_use', models.ForeignKey(verbose_name='Approved use', blank=True, to='celllines.ApprovedUse', null=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line legal',
                'verbose_name_plural': 'Cell line legal',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLineNonIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.OneToOneField(related_name='non_integrating_vector', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line non integrating vector',
                'verbose_name_plural': 'Cell line non integrating vectors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineorganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgstatus', models.IntegerField(null=True, verbose_name='Org status', blank=True)),
                ('orgregistrationdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line organization',
                'verbose_name_plural': 'Cell line organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineorgtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllineorgtype', models.CharField(max_length=45, verbose_name='Cell line org type', blank=True)),
            ],
            options={
                'ordering': ['celllineorgtype'],
                'verbose_name': 'Cell line org type',
                'verbose_name_plural': 'Cell line org types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CellLinePublication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_type', models.CharField(max_length=100, verbose_name='Type', choices=[(b'pubmed', b'PubMed')])),
                ('reference_id', models.CharField(max_length=100, null=True, verbose_name='ID', blank=True)),
                ('reference_url', models.URLField(verbose_name='URL')),
                ('reference_title', models.CharField(max_length=500, verbose_name='Title')),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': ('reference_title',),
                'verbose_name': 'Cell line publication',
                'verbose_name_plural': 'Cell line publications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblink', models.CharField(max_length=45, verbose_name='Weblink', blank=True)),
                ('snpcellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line snp',
                'verbose_name_plural': 'Cell line snps',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnpdetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinesnpgene', models.CharField(max_length=45, verbose_name='Cell line snp gene', blank=True)),
                ('celllinesnpchromosomalposition', models.CharField(max_length=45, verbose_name='Cell line snp chromosomal position', blank=True)),
                ('celllinesnp', models.ForeignKey(verbose_name='Cell line snp', blank=True, to='celllines.Celllinesnp', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line snp details',
                'verbose_name_plural': 'Cell line snp details',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnprslinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsnumber', models.CharField(max_length=45, verbose_name='Rs number', blank=True)),
                ('rslink', models.CharField(max_length=100, verbose_name='Rs link', blank=True)),
                ('celllinesnp', models.ForeignKey(verbose_name='Cel lline snp', blank=True, to='celllines.Celllinesnp', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line snp Rs links',
                'verbose_name_plural': 'Cell line snp Rs links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinestatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinestatus', models.CharField(max_length=50, verbose_name='Cell line status', blank=True)),
            ],
            options={
                'ordering': ['celllinestatus'],
                'verbose_name': 'Cell line status',
                'verbose_name_plural': 'Cell line statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinestrfingerprinting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele1', models.CharField(max_length=45, verbose_name='All ele1', blank=True)),
                ('allele2', models.CharField(max_length=45, verbose_name='All ele2', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line STR finger printing',
                'verbose_name_plural': 'Cell line STR finger printings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinevalue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('potentialuse', models.CharField(max_length=100, verbose_name='Potential use', blank=True)),
                ('valuetosociety', models.CharField(max_length=100, verbose_name='Value to society', blank=True)),
                ('valuetoresearch', models.CharField(max_length=100, verbose_name='Value to research', blank=True)),
                ('othervalue', models.CharField(max_length=100, verbose_name='Other value', blank=True)),
                ('valuecellline', models.OneToOneField(null=True, blank=True, to='celllines.Cellline', verbose_name='Cell line')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line value',
                'verbose_name_plural': 'Cell line values',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celltype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celltype', models.CharField(max_length=100, verbose_name='Celltype', blank=True)),
            ],
            options={
                'ordering': ['celltype'],
                'verbose_name': 'Cell type',
                'verbose_name_plural': 'Cell types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clinicaltreatmentb4donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clinicaltreatmentb4donation', models.CharField(max_length=45, verbose_name='Clininical treatment b4 donation', blank=True)),
            ],
            options={
                'ordering': ['clinicaltreatmentb4donation'],
                'verbose_name': 'Clininical treatment B4 donation',
                'verbose_name_plural': 'Clininical treatment B4 donations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statecounty', models.IntegerField(null=True, verbose_name='State county', blank=True)),
                ('city', models.CharField(max_length=45, verbose_name='City', blank=True)),
                ('street', models.CharField(max_length=45, verbose_name='Street', blank=True)),
                ('buildingnumber', models.CharField(max_length=20, verbose_name='Building number', blank=True)),
                ('suiteoraptordept', models.CharField(max_length=10, null=True, verbose_name='Suite or apt or dept', blank=True)),
                ('officephone', models.CharField(max_length=20, null=True, verbose_name='Office phone', blank=True)),
                ('fax', models.CharField(max_length=20, null=True, verbose_name='Fax', blank=True)),
                ('mobilephone', models.CharField(max_length=20, null=True, verbose_name='Mobile phone', blank=True)),
                ('website', models.CharField(max_length=45, null=True, verbose_name='Website', blank=True)),
                ('emailaddress', models.CharField(max_length=45, null=True, verbose_name='Email address', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacttype', models.CharField(max_length=45, verbose_name='Contact type', blank=True)),
            ],
            options={
                'ordering': ['contacttype'],
                'verbose_name': 'Contact type',
                'verbose_name_plural': 'Contact types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Country')),
                ('code', models.CharField(max_length=3, unique=True, null=True, verbose_name='Country code', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CultureMedium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Culture medium')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Culture medium',
                'verbose_name_plural': 'Culture mediums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CultureMediumOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base', models.CharField(max_length=45, verbose_name='Culture medium base', blank=True)),
                ('serum_concentration', models.IntegerField(null=True, verbose_name='Serum concentration', blank=True)),
                ('cell_line_culture_conditions', models.OneToOneField(related_name='culture_medium_other', verbose_name='Cell line culture conditions', to='celllines.Celllinecultureconditions')),
            ],
            options={
                'ordering': ['base', 'protein_source', 'serum_concentration'],
                'verbose_name': 'Culture medium',
                'verbose_name_plural': 'Culture mediums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Culturesystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('culturesystem', models.CharField(max_length=45, verbose_name='Culture system', blank=True)),
            ],
            options={
                'ordering': ['culturesystem'],
                'verbose_name': 'Culture system',
                'verbose_name_plural': 'Culture systems',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icdcode', models.CharField(max_length=30, unique=True, null=True, verbose_name='DOID', blank=True)),
                ('disease', models.CharField(max_length=45, verbose_name='Disease', blank=True)),
                ('synonyms', models.CharField(max_length=500, null=True, verbose_name='Synonyms', blank=True)),
            ],
            options={
                'ordering': ['disease'],
                'verbose_name': 'Disease',
                'verbose_name_plural': 'Diseases',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cellline', models.IntegerField(null=True, verbose_name='Cell line', blank=True)),
                ('title', models.CharField(max_length=45, verbose_name='Title', blank=True)),
                ('abstract', models.TextField(null=True, verbose_name='Abstract', blank=True)),
                ('documentdepositor', models.IntegerField(null=True, verbose_name='Document depositor', blank=True)),
                ('authors', models.TextField(null=True, verbose_name='Authors', blank=True)),
                ('owner', models.IntegerField(null=True, verbose_name='Owner', blank=True)),
                ('version', models.CharField(max_length=5, verbose_name='Version', blank=True)),
                ('accesslevel', models.IntegerField(null=True, verbose_name='Access level', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documenttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documenttype', models.CharField(max_length=30, verbose_name='Document type', blank=True)),
            ],
            options={
                'ordering': ['documenttype'],
                'verbose_name': 'Document type',
                'verbose_name_plural': 'Document types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamplesid', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('diseaseadditionalinfo', models.CharField(max_length=45, verbose_name='Disease additional info', blank=True)),
                ('providerdonorid', models.CharField(max_length=45, verbose_name='Provider donor id', blank=True)),
                ('cellabnormalkaryotype', models.CharField(max_length=45, verbose_name='Cell abnormal karyotype', blank=True)),
                ('donorabnormalkaryotype', models.CharField(max_length=45, verbose_name='Donor abnormal karyotype', blank=True)),
                ('otherclinicalinformation', models.CharField(max_length=100, verbose_name='Other clinical information', blank=True)),
                ('countryoforigin', models.ForeignKey(verbose_name='Country', blank=True, to='celllines.Country', null=True)),
            ],
            options={
                'ordering': ['biosamplesid'],
                'verbose_name': 'Donor',
                'verbose_name_plural': 'Donors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ebisckeyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cellline', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
                ('document', models.ForeignKey(verbose_name='Document', blank=True, to='celllines.Document', null=True)),
            ],
            options={
                'ordering': ['cellline', 'document', 'ebisckeyword'],
                'verbose_name': 'Ebisc keyword',
                'verbose_name_plural': 'Ebisc keywords',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enzymatically',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Enzymatically')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Enzymatically',
                'verbose_name_plural': 'Enzymatically',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnzymeFree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Enzyme free')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Enzyme free',
                'verbose_name_plural': 'Enzyme free',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='Gender')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Germlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('germlayer', models.CharField(max_length=15, verbose_name='Germ layer', blank=True)),
            ],
            options={
                'ordering': ['germlayer'],
                'verbose_name': 'Germ layer',
                'verbose_name_plural': 'Germ layers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hla', models.CharField(max_length=45, verbose_name='HLA', blank=True)),
            ],
            options={
                'ordering': ['hla'],
                'verbose_name': 'HLA',
                'verbose_name_plural': 'HLAs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Integrating vector')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Integrating vector',
                'verbose_name_plural': 'Integrating vectors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KaryotypeMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Karyotype method')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Karyotype method',
                'verbose_name_plural': 'Karyotype methods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=45, verbose_name='Keyword', blank=True)),
            ],
            options={
                'ordering': ['keyword'],
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('kind', models.CharField(max_length=20, verbose_name='Kind', choices=[(b'gene', 'Gene'), (b'protein', 'Protein')])),
            ],
            options={
                'ordering': ['name', 'kind'],
                'verbose_name': 'Molecule',
                'verbose_name_plural': 'Molecules',
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Morphologymethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphologymethod', models.CharField(max_length=45, verbose_name='Morphology method', blank=True)),
            ],
            options={
                'ordering': ['morphologymethod'],
                'verbose_name': 'Morphology method',
                'verbose_name_plural': 'Morphology methods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NonIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Non-integrating vector')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Non-integrating vector',
                'verbose_name_plural': 'Non-integrating vectors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizationname', models.CharField(max_length=100, unique=True, null=True, verbose_name='Organization name', blank=True)),
                ('organizationshortname', models.CharField(max_length=6, unique=True, null=True, verbose_name='Organization short name', blank=True)),
                ('organizationcontact', models.ForeignKey(verbose_name='Contact', blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': ['organizationname', 'organizationshortname'],
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orgtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgtype', models.CharField(max_length=45, verbose_name='Org type', blank=True)),
            ],
            options={
                'ordering': ['orgtype'],
                'verbose_name': 'Organization type',
                'verbose_name_plural': 'Organization types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PassageMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Passage method')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Passage method',
                'verbose_name_plural': 'Passage methods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.IntegerField(null=True, verbose_name='Organization', blank=True)),
                ('personlastname', models.CharField(max_length=20, verbose_name='Person last name', blank=True)),
                ('personfirstname', models.CharField(max_length=45, verbose_name='Person first name', blank=True)),
                ('personcontact', models.ForeignKey(verbose_name='Contact', blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': ['personlastname', 'personfirstname'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phenotype', models.CharField(max_length=45, verbose_name='Phenotype', blank=True)),
            ],
            options={
                'ordering': ['phenotype'],
                'verbose_name': 'Phenotype',
                'verbose_name_plural': 'Phenotypes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phonecountrycode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phonecountrycode', models.DecimalField(null=True, verbose_name='Phone country code', max_digits=4, decimal_places=0, blank=True)),
            ],
            options={
                'ordering': ['phonecountrycode'],
                'verbose_name': 'Phone country code',
                'verbose_name_plural': 'Phone country codes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcode', models.CharField(max_length=45, verbose_name='Postcode', blank=True)),
                ('district', models.CharField(max_length=20, verbose_name='District')),
            ],
            options={
                'ordering': ['postcode', 'district'],
                'verbose_name': 'Postcode',
                'verbose_name_plural': 'Postcodes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrimaryCellDevelopmentalStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='Primary cell developmental stage')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Primary cell developmental stage',
                'verbose_name_plural': 'Primary cell developmental stages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProteinSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Protein source')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Protein source',
                'verbose_name_plural': 'Protein sources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher', models.CharField(max_length=45, verbose_name='Publisher', blank=True)),
            ],
            options={
                'ordering': ['publisher'],
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod1', models.CharField(max_length=45, verbose_name='Reprogramming method 1', blank=True)),
            ],
            options={
                'ordering': ['reprogrammingmethod1'],
                'verbose_name': 'Reprogramming method 1',
                'verbose_name_plural': 'Reprogramming methods 1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod2', models.CharField(max_length=45, verbose_name='Reprogramming method 2', blank=True)),
            ],
            options={
                'ordering': ['reprogrammingmethod2'],
                'verbose_name': 'Reprogramming method 2',
                'verbose_name_plural': 'Reprogramming methods 2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod3', models.CharField(max_length=45, verbose_name='Reprogramming method 3', blank=True)),
            ],
            options={
                'ordering': ['reprogrammingmethod3'],
                'verbose_name': 'Reprogramming method 3',
                'verbose_name_plural': 'Reprogramming methods 3',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Strfplocus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strfplocus', models.CharField(max_length=45, verbose_name='STR FP locus', blank=True)),
            ],
            options={
                'ordering': ['strfplocus'],
                'verbose_name': 'STR FP locus',
                'verbose_name_plural': 'STR FP loci',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurfaceCoating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Surface coating')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Surface coating',
                'verbose_name_plural': 'Surface coatings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tissuesource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tissuesource', models.CharField(max_length=45, verbose_name='Tissue source', blank=True)),
            ],
            options={
                'ordering': ['tissuesource'],
                'verbose_name': 'Tissue source',
                'verbose_name_plural': 'Tissue sources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transposon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Transposon', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Transposon',
                'verbose_name_plural': 'Transposons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerExpressionProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=100, null=True, verbose_name='Method', blank=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('data_url', models.URLField(null=True, verbose_name='Data URL', blank=True)),
                ('uploaded_data_url', models.URLField(null=True, verbose_name='Uploaded data URL', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_expression_profile', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Expression profile',
                'verbose_name_plural': 'Markerd Undiff - Expression profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerExpressionProfileMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerExpressionProfile')),
                ('molecule', models.ForeignKey(to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerFacs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_facs', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Facs',
                'verbose_name_plural': 'Markerd Undiff - Facs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerFacsMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerFacs')),
                ('molecule', models.ForeignKey(to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerImune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_imune', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Imune',
                'verbose_name_plural': 'Markerd Undiff - Imune',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerImuneMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerImune')),
                ('molecule', models.ForeignKey(to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerMorphology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('data_url', models.URLField(null=True, verbose_name='URL', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_morphology', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Morphology',
                'verbose_name_plural': 'Markerd Undiff - Morphology',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerRtPcr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_rtpcr', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - RtPcr',
                'verbose_name_plural': 'Markerd Undiff - RtPcr',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerRtPcrMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerRtPcr')),
                ('molecule', models.ForeignKey(to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Units')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Units',
                'verbose_name_plural': 'Units',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vectorfreereprogramfactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vectorfreereprogramfactor', models.CharField(max_length=15, verbose_name='Vector free reprogram factor', blank=True)),
                ('referenceid', models.CharField(max_length=45, verbose_name='Referenceid', blank=True)),
            ],
            options={
                'ordering': ['vectorfreereprogramfactor'],
                'verbose_name': 'Vector free reprogram factor',
                'verbose_name_plural': 'Vector free reprogram factors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Virus')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Virus',
                'verbose_name_plural': 'Viruses',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='organizationtype',
            field=models.ForeignKey(verbose_name='Orgtype', blank=True, to='celllines.Orgtype', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='moleculereference',
            unique_together=set([('molecule', 'catalog')]),
        ),
        migrations.AlterUniqueTogether(
            name='molecule',
            unique_together=set([('name', 'kind')]),
        ),
        migrations.AddField(
            model_name='ebisckeyword',
            name='ebisckeyword',
            field=models.ForeignKey(verbose_name='Keyword', blank=True, to='celllines.Keyword', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='gender',
            field=models.ForeignKey(verbose_name='Gender', blank=True, to='celllines.Gender', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='othercelllinefromdonor',
            field=models.ForeignKey(related_name='celllines_othercelllinefromdonor', verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='parentcellline',
            field=models.ForeignKey(related_name='celllines_parentcellline', verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='phenotype',
            field=models.ForeignKey(verbose_name='Phenotype', blank=True, to='celllines.Phenotype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='primarydisease',
            field=models.ForeignKey(verbose_name='Disease', blank=True, to='celllines.Disease', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='documenttype',
            field=models.ForeignKey(verbose_name='Document type', blank=True, to='celllines.Documenttype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='culturemediumother',
            name='protein_source',
            field=models.ForeignKey(verbose_name='Protein source', blank=True, to='celllines.ProteinSource', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='contacttype',
            field=models.ForeignKey(verbose_name='Contact type', blank=True, to='celllines.Contacttype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.ForeignKey(db_column=b'country', verbose_name='Country', to='celllines.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='faxcountrycode',
            field=models.ForeignKey(related_name='contacts_faxcountrycode', verbose_name='Phone country code', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobilecountrycode',
            field=models.ForeignKey(related_name='contacts_mobilecountrycode', verbose_name='Phone country code', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='officephonecountrycode',
            field=models.ForeignKey(related_name='contacts_officephonecountrycode', verbose_name='Phone country code', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='postcode',
            field=models.ForeignKey(db_column=b'postcode', verbose_name='Postcode', to='celllines.Postcode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='locus',
            field=models.ForeignKey(verbose_name='STR fplocus', blank=True, to='celllines.Strfplocus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='strfpcellline',
            field=models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='celllinepublication',
            unique_together=set([('cell_line', 'reference_url')]),
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='celllineorgtype',
            field=models.ForeignKey(verbose_name='Cell line org type', to='celllines.Celllineorgtype'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='organization',
            field=models.ForeignKey(verbose_name='Organization', to='celllines.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='orgcellline',
            field=models.ForeignKey(related_name='organizations', verbose_name='Cell line', to='celllines.Cellline'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='celllineorganization',
            unique_together=set([('orgcellline', 'organization', 'celllineorgtype')]),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='vector',
            field=models.ForeignKey(verbose_name='Non-integrating vector', blank=True, to='celllines.NonIntegratingVector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='jurisdiction',
            field=models.ForeignKey(verbose_name='Jurisdiction', blank=True, to='celllines.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='culturesystem',
            field=models.ForeignKey(verbose_name='Culture system', blank=True, to='celllines.Culturesystem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='labcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline', verbose_name='Cell line'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod1',
            field=models.ForeignKey(verbose_name='Reprogramming method 1', blank=True, to='celllines.Reprogrammingmethod1', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod2',
            field=models.ForeignKey(verbose_name='Reprogramming method 2', blank=True, to='celllines.Reprogrammingmethod2', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod3',
            field=models.ForeignKey(verbose_name='Reprogramming method 3', blank=True, to='celllines.Reprogrammingmethod3', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinekaryotype',
            name='karyotype_method',
            field=models.ForeignKey(verbose_name='Karyotype method', blank=True, to='celllines.KaryotypeMethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='vector',
            field=models.ForeignKey(verbose_name='Integrating vector', blank=True, to='celllines.IntegratingVector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='celllinehla',
            field=models.ForeignKey(verbose_name='Hla', blank=True, to='celllines.Hla', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hlatypingcellline',
            field=models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='primarycelldevelopmentalstage',
            field=models.ForeignKey(verbose_name='Primary cell developmental stage', blank=True, to='celllines.PrimaryCellDevelopmentalStage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineculturemediumsupplement',
            name='unit',
            field=models.ForeignKey(verbose_name='Unit', blank=True, to='celllines.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='culture_medium',
            field=models.ForeignKey(verbose_name='Culture medium', blank=True, to='celllines.CultureMedium', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='enzymatically',
            field=models.ForeignKey(verbose_name='Enzymatically', blank=True, to='celllines.Enzymatically', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='enzymefree',
            field=models.ForeignKey(verbose_name='Enzyme free', blank=True, to='celllines.EnzymeFree', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='passagemethod',
            field=models.ForeignKey(verbose_name='Passage method', blank=True, to='celllines.PassageMethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='surfacecoating',
            field=models.ForeignKey(verbose_name='Surface coating', blank=True, to='celllines.SurfaceCoating', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinecelltype',
            field=models.ForeignKey(verbose_name='Cell type', blank=True, to='celllines.Celltype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinecollection',
            field=models.ForeignKey(verbose_name='Cell line collection', blank=True, to='celllines.Celllinecollection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllineprimarydisease',
            field=models.ForeignKey(verbose_name='Disease', blank=True, to='celllines.Disease', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinestatus',
            field=models.ForeignKey(verbose_name='Cell line status', blank=True, to='celllines.Celllinestatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinetissuesource',
            field=models.ForeignKey(verbose_name='Tissue source', blank=True, to='celllines.Tissuesource', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinetissuetreatment',
            field=models.ForeignKey(verbose_name='Clinical treatment B4 donation', blank=True, to='celllines.Clinicaltreatmentb4donation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='donor',
            field=models.ForeignKey(verbose_name='Donor', blank=True, to='celllines.Donor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='donor_age',
            field=models.ForeignKey(verbose_name='Age', blank=True, to='celllines.AgeRange', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='generator',
            field=models.ForeignKey(related_name='generator_of_cell_lines', verbose_name='Generator', to='celllines.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='owner',
            field=models.ForeignKey(related_name='owner_of_cell_lines', verbose_name='Owner', blank=True, to='celllines.Organization', null=True),
            preserve_default=True,
        ),
    ]
