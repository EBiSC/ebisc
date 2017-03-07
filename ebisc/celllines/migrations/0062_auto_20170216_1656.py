# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0061_auto_20170119_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='donordiseasevariant',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockindisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockinnondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockoutdisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationgeneknockoutnondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationisogenicdisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationisogenicnondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationtransgeneexpressiondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationtransgeneexpressionnondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationvariantdisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationvariantnondisease',
            name='variant_id',
            field=models.IntegerField(null=True, verbose_name='Variant ID', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='donordiseasevariant',
            unique_together=set([('donor_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationgeneknockindisease',
            unique_together=set([('cellline_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationgeneknockinnondisease',
            unique_together=set([('cell_line', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationgeneknockoutdisease',
            unique_together=set([('cellline_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationgeneknockoutnondisease',
            unique_together=set([('cell_line', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationisogenicdisease',
            unique_together=set([('cellline_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationisogenicnondisease',
            unique_together=set([('cell_line', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationtransgeneexpressiondisease',
            unique_together=set([('cellline_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationtransgeneexpressionnondisease',
            unique_together=set([('cell_line', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationvariantdisease',
            unique_together=set([('cellline_disease', 'modification_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationvariantnondisease',
            unique_together=set([('cell_line', 'variant_id')]),
        ),
    ]
