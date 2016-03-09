# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0023_auto_20160127_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinecharacterization',
            name='certificate_of_analysis_flag',
            field=models.NullBooleanField(verbose_name='Certificate of analysis flag'),
        ),
        migrations.AddField(
            model_name='celllinecharacterization',
            name='virology_screening_flag',
            field=models.NullBooleanField(verbose_name='Virology screening flag'),
        ),
    ]
