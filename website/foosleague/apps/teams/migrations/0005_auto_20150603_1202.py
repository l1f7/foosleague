# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_team_players'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('-streak',), 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
    ]
