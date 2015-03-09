# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesslevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accesslevel', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': ['accesslevel'],
                'verbose_name': 'Access level',
                'verbose_name_plural': 'Access levels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Aliquotstatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aliquotstatus', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Approveduse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approveduse', models.CharField(max_length=60, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Batchstatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batchstatus', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Binnedage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('binnedage', models.CharField(max_length=5, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cellline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamplesid', models.CharField(unique=True, max_length=12)),
                ('celllinename', models.CharField(unique=True, max_length=15)),
                ('celllinediseaseaddinfo', models.CharField(max_length=100, blank=True)),
                ('celllinetissuedate', models.DateField(null=True, blank=True)),
                ('celllinenamesynonyms', models.CharField(max_length=1000, blank=True)),
                ('depositorscelllineuri', models.CharField(max_length=45, blank=True)),
                ('celllinecomments', models.CharField(max_length=1000, blank=True)),
                ('celllineupdate', models.DateField(null=True, blank=True)),
                ('celllineecaccurl', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinealiquot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aliquotstatusdate', models.CharField(max_length=20, blank=True)),
                ('aliquotcellline', models.ForeignKey(blank=True, to='celllines.Cellline', null=True)),
                ('aliquotstatus', models.ForeignKey(blank=True, to='celllines.Aliquotstatus', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineannotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllineannotationsource', models.CharField(max_length=45, blank=True)),
                ('celllineannotationsourceid', models.CharField(max_length=45, blank=True)),
                ('celllineannotationsourceversion', models.CharField(max_length=45, blank=True)),
                ('celllineannotation', models.CharField(max_length=1000, blank=True)),
                ('celllineannotationupdate', models.DateField(null=True, blank=True)),
                ('annotationcellline', models.ForeignKey(blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinebatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batchstatusdate', models.CharField(max_length=20, blank=True)),
                ('batchcellline', models.ForeignKey(blank=True, to='celllines.Cellline', null=True)),
                ('batchstatus', models.ForeignKey(blank=True, to='celllines.Batchstatus', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecharacterization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificateofanalysispassage', models.CharField(max_length=5, blank=True)),
                ('hiv1screening', models.IntegerField(null=True, blank=True)),
                ('hiv2screening', models.IntegerField(null=True, blank=True)),
                ('hepititusb', models.IntegerField(null=True, blank=True)),
                ('hepititusc', models.IntegerField(null=True, blank=True)),
                ('mycoplasma', models.IntegerField(null=True, blank=True)),
                ('celllinecharacterizationupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinecollectiontotal', models.IntegerField(null=True, blank=True)),
                ('celllinecollectionupdate', models.DateField(null=True, blank=True)),
                ('celllinecollectionupdatetype', models.IntegerField(null=True, blank=True)),
                ('celllinecollectionupdatedby', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecomments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commentscellline', models.IntegerField(null=True, blank=True)),
                ('celllinecomments', models.TextField(blank=True)),
                ('celllinecommentsupdated', models.DateField(null=True, blank=True)),
                ('celllinecommentsupdatedtype', models.IntegerField(null=True, blank=True)),
                ('celllinecommentsupdatedby', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinecultureconditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedercelltype', models.CharField(max_length=45, blank=True)),
                ('feedercellid', models.CharField(max_length=45, blank=True)),
                ('o2concentration', models.IntegerField(null=True, blank=True)),
                ('co2concentration', models.IntegerField(null=True, blank=True)),
                ('celllinecultureconditionsupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineculturesupplements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplement', models.CharField(max_length=45, blank=True)),
                ('supplementamount', models.CharField(max_length=45, blank=True)),
                ('celllineculturesupplementsupdated', models.DateField(null=True, blank=True)),
                ('celllinecultureconditions', models.ForeignKey(blank=True, to='celllines.Celllinecultureconditions', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinederivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primarycelltypename', models.CharField(max_length=45, blank=True)),
                ('primarycelltypecellfinderid', models.CharField(max_length=45, blank=True)),
                ('selectioncriteriaforclones', models.CharField(max_length=1000, blank=True)),
                ('xenofreeconditions', models.CharField(max_length=4, blank=True)),
                ('derivedundergmp', models.CharField(max_length=4, blank=True)),
                ('availableasclinicalgrade', models.CharField(max_length=4, blank=True)),
                ('celllinederivationupdated', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinediffpotency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passagenumber', models.CharField(max_length=5, blank=True)),
                ('celllinediffpotencyupdated', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinediffpotencymarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinediffpotencymarkerupdate', models.DateField(null=True, blank=True)),
                ('celllinediffpotency', models.ForeignKey(blank=True, to='celllines.Celllinediffpotency', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinediffpotencymolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinediffpotencymarker', models.IntegerField(null=True, blank=True)),
                ('diffpotencymoleculeupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenemutations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblink', models.CharField(max_length=100, blank=True)),
                ('celllinegenemutationsupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenemutationsmolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegenemutationsmoleculeupdate', models.DateField(null=True, blank=True)),
                ('celllinegenemutations', models.ForeignKey(blank=True, to='celllines.Celllinegenemutations', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegeneticmod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegeneticmod', models.CharField(max_length=45, blank=True)),
                ('celllinegeneticmodupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenomeseq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegenomeseqlink', models.CharField(max_length=45, blank=True)),
                ('celllinegenomesequpdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinegenotypingother',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinegenotypingother', models.CharField(max_length=1000, blank=True)),
                ('celllinegenotypingotherupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinehlatyping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinehlaclass', models.IntegerField(null=True, blank=True)),
                ('celllinehlaallele1', models.CharField(max_length=45, blank=True)),
                ('celllinehlaallele2', models.CharField(max_length=45, blank=True)),
                ('celllinehlatypingupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinekaryotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passagenumber', models.CharField(max_length=5, blank=True)),
                ('karyotype', models.CharField(max_length=45, blank=True)),
                ('celllinekaryotypeupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinelab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cryodate', models.DateField(null=True, blank=True)),
                ('expansioninprogress', models.IntegerField(null=True, blank=True)),
                ('funder', models.CharField(max_length=45, blank=True)),
                ('clonenumber', models.IntegerField(null=True, blank=True)),
                ('passagenumber', models.CharField(max_length=5, blank=True)),
                ('culturesystemcomment', models.CharField(max_length=45, blank=True)),
                ('celllinelabupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinelegal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q1donorconsent', models.IntegerField(null=True, blank=True)),
                ('q2donortrace', models.IntegerField(null=True, blank=True)),
                ('q3irbapproval', models.IntegerField(null=True, blank=True)),
                ('q5informedconsentreference', models.CharField(max_length=20, blank=True)),
                ('q6restrictions', models.CharField(max_length=1000, blank=True)),
                ('q7iprestrictions', models.CharField(max_length=1000, blank=True)),
                ('q9applicablelegislationandregulation', models.CharField(max_length=1000, blank=True)),
                ('q10managedaccess', models.CharField(max_length=1000, blank=True)),
                ('celllinelegalupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinemarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineorganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcelllineorganization', models.IntegerField(unique=True)),
                ('orgstatus', models.IntegerField(null=True, blank=True)),
                ('orgregistrationdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllineorgtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllineorgtype', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinepublication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubmedreference', models.CharField(max_length=45, blank=True)),
                ('celllinepublicationdoiurl', models.CharField(max_length=1000, blank=True)),
                ('celllinepublicationupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblink', models.CharField(max_length=45, blank=True)),
                ('celllinesnpupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnpdetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinesnpgene', models.CharField(max_length=45, blank=True)),
                ('celllinesnpchromosomalposition', models.CharField(max_length=45, blank=True)),
                ('celllinesnpdetailsupdate', models.DateField(null=True, blank=True)),
                ('celllinesnp', models.ForeignKey(blank=True, to='celllines.Celllinesnp', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinesnprslinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsnumber', models.CharField(max_length=45, blank=True)),
                ('rslink', models.CharField(max_length=100, blank=True)),
                ('celllinesnprslinksupdate', models.DateField(null=True, blank=True)),
                ('celllinesnp', models.ForeignKey(blank=True, to='celllines.Celllinesnp', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinestatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinestatus', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinestrfingerprinting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele1', models.CharField(max_length=45, blank=True)),
                ('allele2', models.CharField(max_length=45, blank=True)),
                ('celllinestrfpupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinevalue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('potentialuse', models.CharField(max_length=100, blank=True)),
                ('valuetosociety', models.CharField(max_length=100, blank=True)),
                ('valuetoresearch', models.CharField(max_length=100, blank=True)),
                ('othervalue', models.CharField(max_length=100, blank=True)),
                ('celllinevalueupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinevector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vectorexcisable', models.CharField(max_length=4, blank=True)),
                ('celllinevectorupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinevectorfreereprogramming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinevectorfreereprogupate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celllinevectormolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celllinevectormoleculeupdate', models.DateField(null=True, blank=True)),
                ('celllinevector', models.ForeignKey(blank=True, to='celllines.Celllinevector', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celltype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celltype', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clinicaltreatmentb4Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clininicaltreatmentb4donation', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statecounty', models.IntegerField(null=True, blank=True)),
                ('city', models.CharField(max_length=45, blank=True)),
                ('street', models.CharField(max_length=45, blank=True)),
                ('buildingnumber', models.CharField(max_length=20, blank=True)),
                ('suiteoraptordept', models.CharField(max_length=10, blank=True)),
                ('officephone', models.CharField(max_length=20, blank=True)),
                ('fax', models.CharField(max_length=20, blank=True)),
                ('mobilephone', models.CharField(max_length=20, blank=True)),
                ('website', models.CharField(max_length=45, blank=True)),
                ('emailaddress', models.CharField(max_length=45, blank=True)),
                ('contactupdate', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacttype', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=45, blank=True)),
                ('countrycode', models.CharField(max_length=3)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Culturemedium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('culturemediumbase', models.CharField(max_length=45, blank=True)),
                ('serumconcentration', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Culturesystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('culturesystem', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icdcode', models.CharField(unique=True, max_length=10, blank=True)),
                ('disease', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cellline', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=45, blank=True)),
                ('abstract', models.CharField(max_length=1000, blank=True)),
                ('documentdepositor', models.IntegerField(null=True, blank=True)),
                ('authors', models.CharField(max_length=1000, blank=True)),
                ('owner', models.IntegerField(null=True, blank=True)),
                ('version', models.CharField(max_length=5, blank=True)),
                ('accesslevel', models.IntegerField(null=True, blank=True)),
                ('documentupdate', models.IntegerField(null=True, blank=True)),
                ('documentupdatetype', models.IntegerField(null=True, blank=True)),
                ('documentupdatedby', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documenttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documenttype', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hescregdonorid', models.CharField(max_length=3, blank=True)),
                ('diseaseadditionalinfo', models.CharField(max_length=45, blank=True)),
                ('providerdonorid', models.CharField(max_length=45, blank=True)),
                ('cellabnormalkaryotype', models.CharField(max_length=45, blank=True)),
                ('donorabnormalkaryotype', models.CharField(max_length=45, blank=True)),
                ('otherclinicalinformation', models.CharField(max_length=100, blank=True)),
                ('donorupdate', models.DateField(null=True, blank=True)),
                ('age', models.ForeignKey(blank=True, to='celllines.Binnedage', null=True)),
                ('countryoforigin', models.ForeignKey(blank=True, to='celllines.Country', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ebisckeyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ebisckeywordupdate', models.DateField(null=True, blank=True)),
                ('cellline', models.ForeignKey(blank=True, to='celllines.Cellline', null=True)),
                ('document', models.ForeignKey(blank=True, to='celllines.Document', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enzymatically',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enzymatically', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enzymefree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enzymefree', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Germlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('germlayer', models.CharField(max_length=15, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hla', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Karyotypemethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karyotypemethod', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lastupdatetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastupdatetype', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marker', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moleculename', models.CharField(max_length=45, blank=True)),
                ('referencesource', models.CharField(max_length=45, blank=True)),
                ('referencesourceid', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Morphologymethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphologymethod', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizationname', models.CharField(max_length=45, blank=True)),
                ('organizationshortname', models.CharField(unique=True, max_length=6, blank=True)),
                ('organizationupdate', models.DateField(null=True, blank=True)),
                ('organizationcontact', models.ForeignKey(blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orgtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgtype', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Passagemethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passagemethod', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.IntegerField(null=True, blank=True)),
                ('personlastname', models.CharField(max_length=20, blank=True)),
                ('personfirstname', models.CharField(max_length=45, blank=True)),
                ('personupdate', models.DateField(null=True, blank=True)),
                ('personcontact', models.ForeignKey(blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phenotype', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phonecountrycode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phonecountrycode', models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcode', models.CharField(max_length=45, blank=True)),
                ('district', models.CharField(max_length=20)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Primarycelldevelopmentalstage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primarycelldevelopmentalstage', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proteinsource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proteinsource', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod1', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod2', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reprogrammingmethod3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reprogrammingmethod3', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Strfplocus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strfplocus', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surfacecoating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surfacecoating', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tissuesource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tissuesource', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transposon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transposon', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('units', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Useraccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=45, blank=True)),
                ('useraccountupdate', models.DateField(null=True, blank=True)),
                ('accesslevel', models.ForeignKey(blank=True, to='celllines.Accesslevel', null=True)),
                ('organization', models.ForeignKey(blank=True, to='celllines.Organization', null=True)),
                ('person', models.ForeignKey(blank=True, to='celllines.Person', null=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Useraccounttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('useraccounttype', models.CharField(max_length=15)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vector', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vectorfreereprogramfactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vectorfreereprogramfactor', models.CharField(max_length=15, blank=True)),
                ('referenceid', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vectortype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vectortype', models.CharField(max_length=15, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('virus', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'ordering': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='useraccounttype',
            field=models.ForeignKey(blank=True, to='celllines.Useraccounttype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='useraccountupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='useraccountupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='personupdatedby',
            field=models.ForeignKey(related_name='people', blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='personupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='organizationtype',
            field=models.ForeignKey(blank=True, to='celllines.Orgtype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='organizationupdatedby',
            field=models.ForeignKey(related_name='organizations', blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='organizationupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ebisckeyword',
            name='ebisckeyword',
            field=models.ForeignKey(blank=True, to='celllines.Keyword', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ebisckeyword',
            name='ebisckeywordupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ebisckeyword',
            name='ebisckeywordupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='donorupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='donorupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='gender',
            field=models.ForeignKey(blank=True, to='celllines.Gender', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='othercelllinefromdonor',
            field=models.ForeignKey(related_name='celllines_othercelllinefromdonor', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='parentcellline',
            field=models.ForeignKey(related_name='celllines_parentcellline', blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='phenotype',
            field=models.ForeignKey(blank=True, to='celllines.Phenotype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='primarydisease',
            field=models.ForeignKey(blank=True, to='celllines.Disease', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='documenttype',
            field=models.ForeignKey(blank=True, to='celllines.Documenttype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='culturemedium',
            name='proteinsource',
            field=models.ForeignKey(blank=True, to='celllines.Proteinsource', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='contacttype',
            field=models.ForeignKey(blank=True, to='celllines.Contacttype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='contactupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='contactupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.ForeignKey(to='celllines.Country', db_column=b'country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='faxcountrycode',
            field=models.ForeignKey(related_name='contacts_faxcountrycode', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobilecountrycode',
            field=models.ForeignKey(related_name='contacts_mobilecountrycode', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='officephonecountrycode',
            field=models.ForeignKey(related_name='contacts_officephonecountrycode', blank=True, to='celllines.Phonecountrycode', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='postcode',
            field=models.ForeignKey(to='celllines.Postcode', db_column=b'postcode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectormolecule',
            name='celllinevectormoleculeupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectormolecule',
            name='celllinevectormoleculeupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectormolecule',
            name='molecule',
            field=models.ForeignKey(blank=True, to='celllines.Molecule', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogramming',
            name='celllinevectorfreereprogupatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogramming',
            name='celllinevectorfreereprogupatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogramming',
            name='vectorfreecellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogramming',
            name='vectorfreereprogrammingfactor',
            field=models.ForeignKey(blank=True, to='celllines.Vectorfreereprogramfactor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='celllinevectorupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='celllinevectorupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='transposon',
            field=models.ForeignKey(blank=True, to='celllines.Transposon', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='vector',
            field=models.ForeignKey(blank=True, to='celllines.Vector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='vectorcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='vectortype',
            field=models.ForeignKey(blank=True, to='celllines.Vectortype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevector',
            name='virus',
            field=models.ForeignKey(blank=True, to='celllines.Virus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevalue',
            name='celllinevalueupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevalue',
            name='celllinevalueupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinevalue',
            name='valuecellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='celllinestrfpupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='celllinestrfpupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='locus',
            field=models.ForeignKey(blank=True, to='celllines.Strfplocus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinestrfingerprinting',
            name='strfpcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnprslinks',
            name='celllinesnprslinksupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnprslinks',
            name='celllinesnprslinksupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnpdetails',
            name='celllinesnpdetailsupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnpdetails',
            name='celllinesnpdetailsupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnp',
            name='celllinesnpupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnp',
            name='celllinesnpupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinesnp',
            name='snpcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='celllinepublicationupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='celllinepublicationupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='celllinepublisher',
            field=models.ForeignKey(blank=True, to='celllines.Publisher', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinepublication',
            name='publicationcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='celllineorgtype',
            field=models.ForeignKey(blank=True, to='celllines.Celllineorgtype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='organization',
            field=models.ForeignKey(blank=True, to='celllines.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='orgcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='celllinemarker',
            field=models.ForeignKey(blank=True, to='celllines.Marker', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='markercellline',
            field=models.ForeignKey(to='celllines.Cellline', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='morphologymethod',
            field=models.ForeignKey(blank=True, to='celllines.Morphologymethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='celllinelegalupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='celllinelegalupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='legalcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='q4approveduse',
            field=models.ForeignKey(blank=True, to='celllines.Approveduse', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='q8jurisdiction',
            field=models.ForeignKey(blank=True, to='celllines.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='celllinelabupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='celllinelabupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='culturesystem',
            field=models.ForeignKey(blank=True, to='celllines.Culturesystem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='labcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod1',
            field=models.ForeignKey(blank=True, to='celllines.Reprogrammingmethod1', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod2',
            field=models.ForeignKey(blank=True, to='celllines.Reprogrammingmethod2', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelab',
            name='reprogrammingmethod3',
            field=models.ForeignKey(blank=True, to='celllines.Reprogrammingmethod3', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinekaryotype',
            name='celllinekaryotypeupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinekaryotype',
            name='celllinekaryotypeupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinekaryotype',
            name='karyotypecellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinekaryotype',
            name='karyotypemethod',
            field=models.ForeignKey(blank=True, to='celllines.Karyotypemethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='celllinehla',
            field=models.ForeignKey(blank=True, to='celllines.Hla', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='celllinehlatypingupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='celllinehlatypingupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinehlatyping',
            name='hlatypingcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenotypingother',
            name='celllinegenotypingotherupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenotypingother',
            name='celllinegenotypingotherupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenotypingother',
            name='genometypothercellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenomeseq',
            name='celllinegenomesequpdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenomeseq',
            name='celllinegenomesequpdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenomeseq',
            name='genomeseqcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegeneticmod',
            name='celllinegeneticmodupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegeneticmod',
            name='celllinegeneticmodupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegeneticmod',
            name='geneticmodcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutationsmolecule',
            name='celllinegenemutationsmoleculeupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutationsmolecule',
            name='celllinegenemutationsmoleculeupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutationsmolecule',
            name='genemutationsmolecule',
            field=models.ForeignKey(blank=True, to='celllines.Molecule', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutations',
            name='celllinegenemutationsupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutations',
            name='celllinegenemutationsupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinegenemutations',
            name='genemutationscellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymolecule',
            name='diffpotencymolecule',
            field=models.ForeignKey(blank=True, to='celllines.Molecule', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymolecule',
            name='diffpotencymoleculeupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymolecule',
            name='diffpotencymoleculeupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymarker',
            name='celllinediffpotencymarkerupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymarker',
            name='celllinediffpotencymarkerupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotencymarker',
            name='morphologymethod',
            field=models.ForeignKey(blank=True, to='celllines.Morphologymethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotency',
            name='celllinediffpotencyupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotency',
            name='celllinediffpotencyupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotency',
            name='diffpotencycellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinediffpotency',
            name='germlayer',
            field=models.ForeignKey(blank=True, to='celllines.Germlayer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='celllinederivationupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='celllinederivationupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='derivationcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='primarycelldevelopmentalstage',
            field=models.ForeignKey(blank=True, to='celllines.Primarycelldevelopmentalstage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineculturesupplements',
            name='celllineculturesupplementsupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineculturesupplements',
            name='celllineculturesupplementsupdatedtype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineculturesupplements',
            name='supplementamountunit',
            field=models.ForeignKey(blank=True, to='celllines.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='celllinecultureconditionsupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='celllinecultureconditionsupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='cultureconditionscellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='culturemedium',
            field=models.ForeignKey(blank=True, to='celllines.Culturemedium', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='enzymatically',
            field=models.ForeignKey(blank=True, to='celllines.Enzymatically', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='enzymefree',
            field=models.ForeignKey(blank=True, to='celllines.Enzymefree', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='passagemethod',
            field=models.ForeignKey(blank=True, to='celllines.Passagemethod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='surfacecoating',
            field=models.ForeignKey(blank=True, to='celllines.Surfacecoating', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='celllinecharacterizationupdateby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='celllinecharacterizationupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='characterizationcellline',
            field=models.ForeignKey(blank=True, to='celllines.Cellline', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinebatch',
            name='batchstatusupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineannotation',
            name='celllineannotationupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllineannotation',
            name='celllineannotationupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='aliquotupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinecelltype',
            field=models.ForeignKey(blank=True, to='celllines.Celltype', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinecollection',
            field=models.ForeignKey(blank=True, to='celllines.Celllinecollection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinedonor',
            field=models.ForeignKey(blank=True, to='celllines.Donor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllineprimarydisease',
            field=models.ForeignKey(blank=True, to='celllines.Disease', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinestatus',
            field=models.ForeignKey(blank=True, to='celllines.Celllinestatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinetissuesource',
            field=models.ForeignKey(blank=True, to='celllines.Tissuesource', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllinetissuetreatment',
            field=models.ForeignKey(blank=True, to='celllines.Clinicaltreatmentb4Donation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllineupdatedby',
            field=models.ForeignKey(blank=True, to='celllines.Useraccount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cellline',
            name='celllineupdatetype',
            field=models.ForeignKey(blank=True, to='celllines.Lastupdatetype', null=True),
            preserve_default=True,
        ),
    ]
