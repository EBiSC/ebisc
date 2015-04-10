# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPermission',
            fields=[
            ],
            options={
                'verbose_name': 'Access permission',
                'proxy': True,
                'verbose_name_plural': 'Access permissions',
            },
            bases=('auth.permission',),
        ),
    ]
