# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0006_auto_20150310_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='culturesystem',
            options={'ordering': ['culturesystem'], 'verbose_name': 'Culture system', 'verbose_name_plural': 'Culture systems'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': ['gender'], 'verbose_name': 'Gender', 'verbose_name_plural': 'Genders'},
        ),
        migrations.AlterModelOptions(
            name='phenotype',
            options={'ordering': ['phenotype'], 'verbose_name': 'Phenotype', 'verbose_name_plural': 'Phenotypes'},
        ),
        migrations.AlterModelOptions(
            name='phonecountrycode',
            options={'ordering': ['phonecountrycode'], 'verbose_name': 'Phone country code', 'verbose_name_plural': 'Phone country codes'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod1',
            options={'ordering': ['reprogrammingmethod1'], 'verbose_name': 'Reprogramming method 1', 'verbose_name_plural': 'Reprogramming methods 1'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod2',
            options={'ordering': ['reprogrammingmethod2'], 'verbose_name': 'Reprogramming method 2', 'verbose_name_plural': 'Reprogramming methods 2'},
        ),
        migrations.AlterModelOptions(
            name='reprogrammingmethod3',
            options={'ordering': ['reprogrammingmethod3'], 'verbose_name': 'Reprogramming method 3', 'verbose_name_plural': 'Reprogramming methods 3'},
        ),
        migrations.AlterField(
            model_name='phonecountrycode',
            name='phonecountrycode',
            field=models.DecimalField(null=True, verbose_name='Phone country code', max_digits=4, decimal_places=0, blank=True),
            preserve_default=True,
        ),
    ]
