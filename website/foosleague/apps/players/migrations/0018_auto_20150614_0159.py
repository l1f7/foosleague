# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_exposehistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exposehistory',
            old_name='expose',
            new_name='ts_expose',
        ),
    ]
