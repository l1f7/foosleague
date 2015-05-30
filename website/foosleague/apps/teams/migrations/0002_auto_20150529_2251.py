# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='streak',
            field=models.IntegerField(default=0, help_text=b'De-normalized field to help with slack integration', verbose_name='Current Streak'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='trueskill',
            field=models.FloatField(default=20, verbose_name='TrueSkill'),
            preserve_default=True,
        ),
    ]
