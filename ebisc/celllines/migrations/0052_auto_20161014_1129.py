# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celllines', '0051_auto_20161006_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celllinestatus',
            options={'ordering': ['-updated'], 'verbose_name': 'Cell line status', 'verbose_name_plural': 'Cell line statuses'},
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='status',
        ),
        migrations.AddField(
            model_name='celllinestatus',
            name='cell_line',
            field=models.ForeignKey(related_name='statuses', default='', verbose_name='Cell line', to='celllines.Cellline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinestatus',
            name='comment',
            field=models.TextField(null=True, verbose_name='Comment', blank=True),
        ),
        migrations.AddField(
            model_name='celllinestatus',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 14, 9, 29, 10, 137147, tzinfo=utc), verbose_name='Updated', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celllinestatus',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='celllinestatus',
            name='status',
            field=models.CharField(default=b'not_available', max_length=50, verbose_name='Status', choices=[(b'not_available', 'Not available'), (b'at_ecacc', 'Stocked by ECACC'), (b'expand_to_order', 'Expand to order'), (b'restricted_distribution', 'Restricted distribution'), (b'recalled', 'Recalled'), (b'withdrawn', 'Withdrawn')]),
        ),
    ]
