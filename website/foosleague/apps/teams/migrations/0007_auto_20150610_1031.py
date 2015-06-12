# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20150604_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='best_streak',
            field=models.IntegerField(default=0, help_text=b'The best streak every acheived by this team', verbose_name='Best Streak'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='best_streak_date',
            field=models.DateTimeField(help_text=b'The date of the last win', null=True, verbose_name='Best Streak Date', blank=True),
            preserve_default=True,
        ),
    ]
