# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20150530_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AlterField(
            model_name='player',
            name='slack_username',
            field=models.CharField(default=b'', help_text=b'This will be used for any slack integrations', max_length=100, verbose_name='Slack  Username', blank=True),
            preserve_default=True,
        ),
    ]
