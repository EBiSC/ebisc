# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0028_auto_20160229_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vectorfreereprogrammingfactor',
            options={'ordering': ['name'], 'verbose_name': 'Vector free reprogram factor', 'verbose_name_plural': 'Vector free reprogram factors'},
        ),
        migrations.RenameField(
            model_name='vectorfreereprogrammingfactor',
            old_name='vector_free_reprogramming_factor',
            new_name='name',
        ),
    ]
