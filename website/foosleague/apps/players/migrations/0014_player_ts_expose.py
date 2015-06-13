# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0013_auto_20150612_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ts_expose',
            field=models.FloatField(default=0, help_text=b'Gets regenerated after ever match', verbose_name='TrueSkill Expose'),
            preserve_default=True,
        ),
    ]
