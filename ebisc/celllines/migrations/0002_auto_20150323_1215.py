# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellline',
            name='celllineaccepted',
            field=models.CharField(default=b'pending', max_length=10, verbose_name='Cell line accepted', choices=[(b'pending', 'Pending'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllinetissuedate',
            field=models.DateField(null=True, verbose_name='Cell line tissue date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cellline',
            name='celllineupdate',
            field=models.DateField(null=True, verbose_name='Cell line updated', blank=True),
            preserve_default=True,
        ),
    ]
