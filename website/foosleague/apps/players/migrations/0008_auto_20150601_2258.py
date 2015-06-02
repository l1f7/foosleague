# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_player_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'players', max_length=400, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
