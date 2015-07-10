# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_remove_stathistory_ts_expose'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rfid_code',
            field=models.CharField(default=b'', help_text=b'RFID Card number', max_length=20, verbose_name='RFID Code', blank=True),
            preserve_default=True,
        ),
    ]
