# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='value',
            field=models.IntegerField(default=1, help_text=b'corrections will be stored as -1', verbose_name='Value'),
            preserve_default=True,
        ),
    ]
