# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0081_auto_20170905_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinevalue',
            name='cell_line',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_type',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='fax_country_code',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mobile_country_code',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='office_phone_country_code',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='document',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='person',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='access_and_use_agreement',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='access_and_use_agreement_md5',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='access_and_use_agreement_participant',
        ),
        migrations.RemoveField(
            model_name='cellline',
            name='access_and_use_agreement_participant_md5',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact',
        ),
        migrations.DeleteModel(
            name='CelllineValue',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ContactType',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='PhoneCountryCode',
        ),
        migrations.DeleteModel(
            name='Postcode',
        ),
    ]
