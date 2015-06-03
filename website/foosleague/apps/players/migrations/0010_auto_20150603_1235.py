# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_auto_20150603_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ts_mu',
            field=models.FloatField(default=25, help_text=b'higher the better', verbose_name='TrueSkill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='ts_sigma',
            field=models.FloatField(default=8.333, help_text=b'basically an indicator of accuracy', verbose_name='TrueSkill Sigma'),
            preserve_default=True,
        ),
    ]
