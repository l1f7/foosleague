# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'Season', 'verbose_name_plural': 'Seasons'},
        ),
    ]
