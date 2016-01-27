# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0021_auto_20160127_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='available_for_sale_at_ecacc',
            field=models.BooleanField(default=False, verbose_name='Available for sale on ECACC'),
        ),
    ]
