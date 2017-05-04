# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Position')),
                ('question', models.CharField(max_length=1000, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name': 'FAQ Category',
                'verbose_name_plural': 'FAQ Categories',
            },
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(related_name='faqs', verbose_name='Category', to='cms.FaqCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='faq',
            unique_together=set([('question', 'category')]),
        ),
    ]
