# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0007_leaguemember_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='fooscoin_earn_loss',
            field=models.FloatField(default=0, verbose_name='Fooscoin earned per loss'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='league',
            name='fooscoin_match_win',
            field=models.FloatField(default=10, verbose_name='Fooscoin earned per win'),
            preserve_default=True,
        ),
    ]
