# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe5\x90\x8d\xe5\xad\x97')),
                ('cards', models.CharField(max_length=1000, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe6\x89\x8b\xe7\x89\x8c')),
                ('playerId', models.IntegerField(default=0, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6id')),
            ],
        ),
        migrations.CreateModel(
            name='PlayersInRunFast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player', models.ForeignKey(to='runfast.Player')),
            ],
        ),
        migrations.CreateModel(
            name='RunFast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('time', models.DateTimeField(verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe6\x97\xb6\xe9\x97\xb4')),
                ('currentCards', models.CharField(max_length=1000, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe6\x89\x93\xe5\x87\xba\xe7\x9a\x84\xe6\x89\x8b\xe7\x89\x8c')),
                ('currentTurn', models.IntegerField(default=0, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe8\xb0\x81\xe6\x89\x93')),
                ('currentPlayedId', models.IntegerField(default=0, verbose_name=b'\xe5\x9c\xba\xe4\xb8\x8a\xe7\x9a\x84\xe7\x89\x8c\xe6\x98\xaf\xe8\xb0\x81\xe6\x89\x93\xe7\x9a\x84')),
                ('players', models.ManyToManyField(to='runfast.Player', through='runfast.PlayersInRunFast')),
            ],
        ),
        migrations.AddField(
            model_name='playersinrunfast',
            name='runfast',
            field=models.ForeignKey(to='runfast.RunFast'),
        ),
    ]
