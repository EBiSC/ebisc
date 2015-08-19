# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0019_cellline_cellline_alternate_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellline',
            name='cellline_alternate_names',
        ),
    ]
