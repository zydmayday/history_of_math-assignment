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
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe6\xa0\x87\xe9\xa2\x98')),
                ('event', models.TextField(max_length=1000, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6')),
                ('post_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
        ),
    ]
