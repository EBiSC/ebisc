# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0024_auto_20160219_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='rock_inhibitor_used_at_cryo',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name='Rock inhibitor (Y27632) used at cryo', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='rock_inhibitor_used_at_passage',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name='Rock inhibitor (Y27632) used at passage', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
        ),
        migrations.AddField(
            model_name='celllinecultureconditions',
            name='rock_inhibitor_used_at_thaw',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name='Rock inhibitor (Y27632) used at thaw', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
        ),
    ]
