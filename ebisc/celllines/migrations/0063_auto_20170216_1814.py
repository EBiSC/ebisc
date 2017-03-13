# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0062_auto_20170216_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='donordiseasevariant',
            name='variant_id',
            field=models.IntegerField(null=True, verbose_name='Variant ID', blank=True),
        ),
        migrations.AddField(
            model_name='modificationvariantnondisease',
            name='modification_id',
            field=models.IntegerField(null=True, verbose_name='Modification ID', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='donordiseasevariant',
            unique_together=set([('donor_disease', 'variant_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='modificationvariantnondisease',
            unique_together=set([('cell_line', 'modification_id')]),
        ),
        migrations.RemoveField(
            model_name='donordiseasevariant',
            name='modification_id',
        ),
        migrations.RemoveField(
            model_name='modificationvariantnondisease',
            name='variant_id',
        ),
    ]
