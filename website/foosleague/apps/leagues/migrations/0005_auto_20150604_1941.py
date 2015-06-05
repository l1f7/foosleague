# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20150604_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='slack_channel',
            field=models.CharField(default=b'', help_text=b'Slack channel you would like foosleague to broadcast to.', max_length=50, verbose_name='Slack Channel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='slack_token',
            field=models.CharField(default=b'', help_text=b'Slack Bot Authentication Token', max_length=100, verbose_name='Slack Token', blank=True),
            preserve_default=True,
        ),
    ]
