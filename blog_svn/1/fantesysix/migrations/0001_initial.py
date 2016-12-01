# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guest_card', models.CharField(max_length=9999, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe6\x89\x8b\xe7\x89\x8c')),
                ('own_card', models.CharField(max_length=9999, verbose_name=b'\xe7\xa8\x8b\xe5\xba\x8f\xe6\x89\x8b\xe7\x89\x8c')),
                ('guest_score', models.IntegerField(verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe5\xbe\x97\xe5\x88\x86')),
                ('own_score', models.CharField(max_length=9999, verbose_name=b'\xe7\xa8\x8b\xe5\xba\x8f\xe5\xbe\x97\xe5\x88\x86')),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryDealCards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deal_cards', models.CharField(max_length=9999, verbose_name=b'\xe5\x8e\x86\xe5\x8f\xb2\xe7\x89\x8c\xe7\xbb\x84')),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Hypothesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hypothesis', models.CharField(max_length=9999, verbose_name=b'\xe5\x8f\x82\xe6\x95\xb0')),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
