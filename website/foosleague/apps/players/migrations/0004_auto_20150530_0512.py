# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20150530_0512'),
        ('players', '0003_player_trueskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fooscoin',
            field=models.FloatField(default=500.0, verbose_name='FoosCoin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='slack_username',
            field=models.CharField(default=b'', help_text=b'This will be used for any slack integrations', max_length=100, verbose_name='Slack Username'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, to='teams.Team', null=True),
            preserve_default=True,
        ),
    ]
