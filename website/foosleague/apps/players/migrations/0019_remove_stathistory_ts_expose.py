# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0018_auto_20150614_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stathistory',
            name='ts_expose',
        ),
    ]
