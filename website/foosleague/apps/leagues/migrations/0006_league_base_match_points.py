# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_auto_20150604_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='base_match_points',
            field=models.IntegerField(default=25, help_text=b'Base match points to be used to calculate leaderboards'),
            preserve_default=True,
        ),
    ]
