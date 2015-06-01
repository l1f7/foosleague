# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_team_players'),
        ('matches', '0002_auto_20150529_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', blank=True, to='teams.Team', null=True),
            preserve_default=True,
        ),
    ]
