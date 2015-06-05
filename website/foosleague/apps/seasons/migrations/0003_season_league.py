# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_auto_20150604_1941'),
        ('seasons', '0002_auto_20150530_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='league',
            field=models.ForeignKey(default=1, to='leagues.League'),
            preserve_default=True,
        ),
    ]
