# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_auto_20150613_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='stathistory',
            name='ts_expose',
            field=models.FloatField(default=0, help_text=b'Leaderboard', verbose_name='TrueSkill Expose'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stathistory',
            name='ts_sigma',
            field=models.FloatField(default=8.3333, help_text=b'Basically an indicator of accuracy', verbose_name='TrueSkill Sigma'),
            preserve_default=True,
        ),
    ]
