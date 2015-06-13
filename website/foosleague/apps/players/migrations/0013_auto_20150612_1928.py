# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0012_auto_20150612_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stathistory',
            name='season_points',
            field=models.IntegerField(null=True, verbose_name='Season Points', blank=True),
            preserve_default=True,
        ),
    ]
