# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runfast', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playersinrunfast',
            name='player',
        ),
        migrations.RemoveField(
            model_name='playersinrunfast',
            name='runfast',
        ),
        migrations.RemoveField(
            model_name='runfast',
            name='currentCards',
        ),
        migrations.RemoveField(
            model_name='runfast',
            name='currentPlayedId',
        ),
        migrations.RemoveField(
            model_name='runfast',
            name='currentTurn',
        ),
        migrations.RemoveField(
            model_name='runfast',
            name='players',
        ),
        migrations.AddField(
            model_name='runfast',
            name='winner',
            field=models.CharField(default=datetime.datetime(2016, 10, 3, 7, 17, 6, 688346, tzinfo=utc), max_length=100, verbose_name=b'\xe8\x83\x9c\xe8\x80\x85'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='PlayersInRunFast',
        ),
    ]
