# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0019_auto_20150312_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllinelab',
            name='labcellline',
            field=models.OneToOneField(null=True, blank=True, to='celllines.Cellline'),
            preserve_default=True,
        ),
    ]
