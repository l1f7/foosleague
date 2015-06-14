# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0014_player_ts_expose'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('-ts_expose',), 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.AddField(
            model_name='stathistory',
            name='fooscoin',
            field=models.FloatField(null=True, verbose_name='Fooscoin', blank=True),
            preserve_default=True,
        ),
    ]
