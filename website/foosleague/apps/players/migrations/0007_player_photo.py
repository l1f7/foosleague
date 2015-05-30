# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20150530_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'players', max_length=400, verbose_name='Photo'),
            preserve_default=True,
        ),
    ]
