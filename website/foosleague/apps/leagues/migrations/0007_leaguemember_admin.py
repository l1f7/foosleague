# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0006_league_base_match_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguemember',
            name='admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
