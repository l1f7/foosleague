# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150529_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='trueskill',
            field=models.FloatField(default=20, verbose_name='TrueSkill'),
            preserve_default=True,
        ),
    ]
