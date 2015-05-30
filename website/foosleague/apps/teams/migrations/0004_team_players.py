# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20150530_1307'),
        ('teams', '0003_auto_20150530_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='players.Player'),
            preserve_default=True,
        ),
    ]
