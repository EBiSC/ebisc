# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0010_auto_20150310_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donor',
            options={'ordering': ['hescregdonorid'], 'verbose_name': 'Donor', 'verbose_name_plural': 'Donors'},
        ),
        migrations.AlterModelOptions(
            name='hla',
            options={'ordering': [], 'verbose_name': 'HLA', 'verbose_name_plural': 'HLAs'},
        ),
        migrations.AlterField(
            model_name='donor',
            name='hescregdonorid',
            field=models.CharField(max_length=3, verbose_name='Hescreg donor ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hla',
            name='hla',
            field=models.CharField(max_length=45, verbose_name='HLA', blank=True),
            preserve_default=True,
        ),
    ]
