# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0002_auto_20150309_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='celllinecomments',
            field=models.TextField(null=True, verbose_name='Celllinecomments', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllineecaccurl',
            field=models.URLField(null=True, verbose_name='Celllineecaccurl', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinenamesynonyms',
            field=models.TextField(null=True, verbose_name='Celllinenamesynonyms', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllineannotation',
            name='celllineannotation',
            field=models.TextField(null=True, verbose_name='Celllineannotation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinederivation',
            name='selectioncriteriaforclones',
            field=models.TextField(null=True, verbose_name='Selectioncriteriaforclones', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinegenotypingother',
            name='celllinegenotypingother',
            field=models.TextField(null=True, verbose_name='Celllinegenotypingother', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q10managedaccess',
            field=models.TextField(null=True, verbose_name='Q10managedaccess', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q6restrictions',
            field=models.TextField(null=True, verbose_name='Q6restrictions', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q7iprestrictions',
            field=models.TextField(null=True, verbose_name='Q7iprestrictions', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='q9applicablelegislationandregulation',
            field=models.TextField(null=True, verbose_name='Q9applicablelegislationandregulation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinepublication',
            name='celllinepublicationdoiurl',
            field=models.URLField(null=True, verbose_name='Celllinepublicationdoiurl', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='abstract',
            field=models.TextField(null=True, verbose_name='Abstract', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='authors',
            field=models.TextField(null=True, verbose_name='Authors', blank=True),
            preserve_default=True,
        ),
    ]
