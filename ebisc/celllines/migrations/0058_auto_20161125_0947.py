# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0057_auto_20161116_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorDisease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease_not_normalised', models.CharField(max_length=500, null=True, verbose_name='Disease name - not normalised', blank=True)),
                ('primary_disease', models.BooleanField(default=False, verbose_name='Primary disease')),
                ('disease_stage', models.CharField(max_length=100, null=True, verbose_name='Disease stage', blank=True)),
                ('affected_status', models.CharField(max_length=12, null=True, verbose_name='Affected status', blank=True)),
                ('carrier', models.CharField(max_length=12, null=True, verbose_name='Carrier', blank=True)),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
                ('disease', models.ForeignKey(verbose_name='Diagnosed disease', blank=True, to='celllines.Disease', null=True)),
                ('donor', models.ForeignKey(related_name='diseases', verbose_name='Donor', to='celllines.Donor')),
            ],
            options={
                'ordering': ['disease'],
                'verbose_name': 'Donor disease',
                'verbose_name_plural': 'Donor diseases',
            },
        ),
        migrations.AddField(
            model_name='celllinedisease',
            name='carrier',
            field=models.CharField(max_length=12, null=True, verbose_name='Carrier', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='donordisease',
            unique_together=set([('donor', 'disease', 'disease_not_normalised')]),
        ),
    ]
