# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0014_auto_20150312_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicaltreatmentb4donation',
            old_name='clininicaltreatmentb4donation',
            new_name='clinicaltreatmentb4donation',
        ),
    ]
