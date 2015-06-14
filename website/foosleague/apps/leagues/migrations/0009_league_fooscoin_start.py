# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_auto_20150613_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='fooscoin_start',
            field=models.FloatField(default=200, help_text=b'the amount of fooscoin players start with', verbose_name='Fooscoin Start'),
            preserve_default=True,
        ),
    ]
