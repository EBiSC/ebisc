# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0009_auto_20150310_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['organizationname', 'organizationshortname'], 'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizationname',
            field=models.CharField(max_length=45, unique=True, null=True, verbose_name='Organization name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizationshortname',
            field=models.CharField(max_length=6, unique=True, null=True, verbose_name='Organization short name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizationupdate',
            field=models.DateField(null=True, verbose_name='Organization update', blank=True),
            preserve_default=True,
        ),
    ]
