# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20150604_1933'),
        ('matches', '0003_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='league',
            field=models.ForeignKey(default=1, verbose_name='League', to='leagues.League'),
            preserve_default=False,
        ),
    ]
