# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0003_season_league'),
        ('players', '0020_player_rfid_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposehistory',
            name='season',
            field=models.ForeignKey(default=1, blank=True, to='seasons.Season', null=True),
            preserve_default=True,
        ),
    ]
