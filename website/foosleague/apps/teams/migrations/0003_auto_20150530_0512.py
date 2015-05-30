# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150529_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_2',
        ),
    ]
