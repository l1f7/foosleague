# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20150530_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slack_username',
            field=models.CharField(default=b'', help_text=b'This will be used for any slack integrations', max_length=100, verbose_name='Slack Username', blank=True),
            preserve_default=True,
        ),
    ]
