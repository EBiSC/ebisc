# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0031_auto_20160229_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='methods',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=50), null=True, verbose_name='Methods used', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='silenced',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name='Have the reprogramming vectors been silenced', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='silenced_notes',
            field=models.TextField(null=True, verbose_name='Notes on reprogramming vector silencing', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='detectable',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name='Is reprogramming vector detectable', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='detectable_notes',
            field=models.TextField(null=True, verbose_name='Notes on reprogramming vector detection', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='methods',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=50), null=True, verbose_name='Methods used', blank=True),
        ),
    ]
