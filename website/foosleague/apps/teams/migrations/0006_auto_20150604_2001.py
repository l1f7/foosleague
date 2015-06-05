# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_auto_20150604_1941'),
        ('teams', '0005_auto_20150603_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='trueskill',
            new_name='trueskill_mu',
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(default=1, verbose_name='League', to='leagues.League'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='trueskill_sigma',
            field=models.FloatField(default=8.33, verbose_name='TrueSkill Sigma'),
            preserve_default=True,
        ),
    ]
