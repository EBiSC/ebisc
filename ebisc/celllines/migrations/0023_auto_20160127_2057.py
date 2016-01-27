# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0022_cellline_available_for_sale_at_ecacc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celllineethics',
            name='consent_prevents_availiability_to_worldwide_research',
            field=models.NullBooleanField(verbose_name='Consent prevents availability to worldwide research'),
        ),
    ]
