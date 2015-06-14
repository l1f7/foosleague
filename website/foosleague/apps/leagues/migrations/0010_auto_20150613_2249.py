# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0009_league_fooscoin_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='fooscoin_earn_loss',
            new_name='fooscoin_for_loss',
        ),
        migrations.RenameField(
            model_name='league',
            old_name='fooscoin_match_win',
            new_name='fooscoin_for_win',
        ),
        migrations.AlterField(
            model_name='league',
            name='fooscoin_start',
            field=models.FloatField(default=200, help_text=b'The amount of fooscoin players start with', verbose_name='Fooscoin Starting Value'),
            preserve_default=True,
        ),
    ]
