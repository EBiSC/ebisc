# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0073_celllinecharacterizationmarkerexpression_celllinecharacterizationmarkerexpressionmethod_celllinechar'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinecharacterizationmarkerexpression',
            name='marker_id',
            field=models.IntegerField(default=0, verbose_name='Marker ID'),
        ),
    ]
