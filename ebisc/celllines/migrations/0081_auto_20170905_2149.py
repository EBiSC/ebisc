# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0080_auto_20170725_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorRelatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(max_length=200, null=True, verbose_name='Type of relation', blank=True)),
                ('donor', models.ForeignKey(related_name='relatives', verbose_name='Donor', to='celllines.Donor')),
                ('related_donor', models.ForeignKey(related_name='relative_of', verbose_name='Relative', to='celllines.Donor')),
            ],
            options={
                'ordering': ['related_donor'],
                'verbose_name': 'Donor relatives',
                'verbose_name_plural': 'Donor relatives',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='comparator_cell_line',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='comparator_cell_line_relation',
        ),
        migrations.AlterUniqueTogether(
            name='donorrelatives',
            unique_together=set([('donor', 'related_donor')]),
        ),
    ]
