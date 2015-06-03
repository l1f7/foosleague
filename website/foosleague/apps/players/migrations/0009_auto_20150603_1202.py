# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20150601_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('nickname', 'user'), 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.RemoveField(
            model_name='player',
            name='trueskill',
        ),
        migrations.AddField(
            model_name='player',
            name='ts_mu',
            field=models.FloatField(default=20, help_text=b'higher the better', verbose_name='TrueSkill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='ts_sigma',
            field=models.FloatField(default=10, help_text=b'basically an indicator of accuracy', verbose_name='TrueSkill Sigma'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='slack_username',
            field=models.CharField(default=b'', help_text=b'This will be used for any slack integrations', max_length=100, verbose_name='Slack Username', blank=True),
            preserve_default=True,
        ),
    ]
