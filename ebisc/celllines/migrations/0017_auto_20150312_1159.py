# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0016_auto_20150312_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='emailaddress',
            field=models.CharField(max_length=45, null=True, verbose_name='Email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(max_length=20, null=True, verbose_name='Fax', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobilephone',
            field=models.CharField(max_length=20, null=True, verbose_name='Mobile phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='officephone',
            field=models.CharField(max_length=20, null=True, verbose_name='Office phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.CharField(max_length=45, null=True, verbose_name='Website', blank=True),
            preserve_default=True,
        ),
    ]
