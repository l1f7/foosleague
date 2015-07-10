# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_match_completed_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ('created',), 'verbose_name': 'Goal', 'verbose_name_plural': 'Goals'},
        ),
    ]
