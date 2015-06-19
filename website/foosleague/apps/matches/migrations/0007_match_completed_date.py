# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_auto_20150616_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='completed_date',
            field=models.DateTimeField(null=True, verbose_name='Completed Date', blank=True),
            preserve_default=True,
        ),
    ]
