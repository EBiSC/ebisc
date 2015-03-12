# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0015_auto_20150312_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinicaltreatmentb4donation',
            options={'ordering': ['clinicaltreatmentb4donation'], 'verbose_name': 'Clininical treatment b4 donation', 'verbose_name_plural': 'Clininical treatment b4 donations'},
        ),
        migrations.AlterModelOptions(
            name='lastupdatetype',
            options={'ordering': ['lastupdatetype'], 'verbose_name': 'Last update type', 'verbose_name_plural': 'Last update types'},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'ordering': ['username'], 'verbose_name': 'User account', 'verbose_name_plural': 'User accounts'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='suiteoraptordept',
            field=models.CharField(max_length=10, null=True, verbose_name='Suite or apt or dept', blank=True),
            preserve_default=True,
        ),
    ]
