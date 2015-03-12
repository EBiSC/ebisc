# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0020_auto_20150312_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliquotstatus',
            options={'ordering': ['aliquotstatus'], 'verbose_name': 'Aliquot status', 'verbose_name_plural': 'Aliquot statuses'},
        ),
        migrations.AlterModelOptions(
            name='approveduse',
            options={'ordering': ['approveduse'], 'verbose_name': 'Approved use', 'verbose_name_plural': 'Approved uses'},
        ),
        migrations.AlterModelOptions(
            name='batchstatus',
            options={'ordering': ['batchstatus'], 'verbose_name': 'Batch status', 'verbose_name_plural': 'Batch statuses'},
        ),
        migrations.AlterModelOptions(
            name='cellline',
            options={'ordering': ['biosamplesid'], 'verbose_name': 'Cell line', 'verbose_name_plural': 'Cell lines'},
        ),
        migrations.AlterModelOptions(
            name='celllineorgtype',
            options={'ordering': ['celllineorgtype'], 'verbose_name': 'Cell line org type', 'verbose_name_plural': 'Cell line org types'},
        ),
        migrations.AlterModelOptions(
            name='contacttype',
            options={'ordering': ['contacttype'], 'verbose_name': 'Contact type', 'verbose_name_plural': 'Contact types'},
        ),
        migrations.AlterModelOptions(
            name='culturemedium',
            options={'ordering': ['culturemediumbase'], 'verbose_name': 'Culture medium', 'verbose_name_plural': 'Culture mediums'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['title'], 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'ordering': ['documenttype'], 'verbose_name': 'Document type', 'verbose_name_plural': 'Document types'},
        ),
        migrations.AlterModelOptions(
            name='ebisckeyword',
            options={'ordering': ['cellline', 'document', 'ebisckeyword'], 'verbose_name': 'Ebisc keyword', 'verbose_name_plural': 'Ebisc keywords'},
        ),
        migrations.AlterModelOptions(
            name='enzymatically',
            options={'ordering': ['enzymatically'], 'verbose_name': 'Enzymatically', 'verbose_name_plural': 'Enzymatically'},
        ),
        migrations.AlterModelOptions(
            name='enzymefree',
            options={'ordering': ['enzymefree'], 'verbose_name': 'Enzyme free', 'verbose_name_plural': 'Enzyme free'},
        ),
        migrations.AlterModelOptions(
            name='germlayer',
            options={'ordering': ['germlayer'], 'verbose_name': 'Germ layer', 'verbose_name_plural': 'Germ layers'},
        ),
        migrations.AlterModelOptions(
            name='hla',
            options={'ordering': ['hla'], 'verbose_name': 'HLA', 'verbose_name_plural': 'HLAs'},
        ),
        migrations.AlterModelOptions(
            name='karyotypemethod',
            options={'ordering': ['karyotypemethod'], 'verbose_name': 'Karyotype method', 'verbose_name_plural': 'Karyotype methods'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['keyword'], 'verbose_name': 'Keyword', 'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='marker',
            options={'ordering': ['marker'], 'verbose_name': 'Marker', 'verbose_name_plural': 'Markers'},
        ),
        migrations.AlterModelOptions(
            name='molecule',
            options={'ordering': ['moleculename'], 'verbose_name': 'Molecule', 'verbose_name_plural': 'Molecules'},
        ),
        migrations.AlterModelOptions(
            name='morphologymethod',
            options={'ordering': ['morphologymethod'], 'verbose_name': 'Morphology method', 'verbose_name_plural': 'Morphology methods'},
        ),
        migrations.AlterModelOptions(
            name='orgtype',
            options={'ordering': ['orgtype'], 'verbose_name': 'Organization type', 'verbose_name_plural': 'Organization types'},
        ),
        migrations.AlterModelOptions(
            name='passagemethod',
            options={'ordering': ['passagemethod'], 'verbose_name': 'Passage method', 'verbose_name_plural': 'Passage methods'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['personlastname', 'personfirstname'], 'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='postcode',
            options={'ordering': ['postcode', 'district'], 'verbose_name': 'Postcode', 'verbose_name_plural': 'Postcodes'},
        ),
        migrations.AlterModelOptions(
            name='primarycelldevelopmentalstage',
            options={'ordering': ['primarycelldevelopmentalstage'], 'verbose_name': 'Primary cell developmental stage', 'verbose_name_plural': 'Primary cell developmental stages'},
        ),
        migrations.AlterModelOptions(
            name='proteinsource',
            options={'ordering': ['proteinsource'], 'verbose_name': 'Protein source', 'verbose_name_plural': 'Protein sources'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['publisher'], 'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
        migrations.AlterModelOptions(
            name='strfplocus',
            options={'ordering': ['strfplocus'], 'verbose_name': 'STR FP locus', 'verbose_name_plural': 'STR FP loci'},
        ),
        migrations.AlterModelOptions(
            name='surfacecoating',
            options={'ordering': ['surfacecoating'], 'verbose_name': 'Surface coating', 'verbose_name_plural': 'Surface coatings'},
        ),
        migrations.AlterModelOptions(
            name='transposon',
            options={'ordering': ['transposon'], 'verbose_name': 'Transposon', 'verbose_name_plural': 'Transposons'},
        ),
        migrations.AlterModelOptions(
            name='units',
            options={'ordering': ['units'], 'verbose_name': 'Units', 'verbose_name_plural': 'Units'},
        ),
        migrations.AlterModelOptions(
            name='useraccounttype',
            options={'ordering': ['useraccounttype'], 'verbose_name': 'User account type', 'verbose_name_plural': 'User account types'},
        ),
        migrations.AlterModelOptions(
            name='vector',
            options={'ordering': ['vector'], 'verbose_name': 'Vector', 'verbose_name_plural': 'Vectors'},
        ),
        migrations.AlterModelOptions(
            name='vectorfreereprogramfactor',
            options={'ordering': ['vectorfreereprogramfactor'], 'verbose_name': 'Vector free reprogram factor', 'verbose_name_plural': 'Vector free reprogram factors'},
        ),
        migrations.AlterModelOptions(
            name='vectortype',
            options={'ordering': ['vectortype'], 'verbose_name': 'Vector type', 'verbose_name_plural': 'Vector types'},
        ),
        migrations.AlterModelOptions(
            name='virus',
            options={'ordering': ['virus'], 'verbose_name': 'Virus', 'verbose_name_plural': 'Viruses'},
        ),
        migrations.AlterField(
            model_name='celllineorganization',
            name='orgcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
    ]
