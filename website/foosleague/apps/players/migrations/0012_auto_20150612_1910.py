# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0011_auto_20150612_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stathistory',
            name='match',
            field=models.ForeignKey(blank=True, to='matches.Match', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stathistory',
            name='season',
            field=models.ForeignKey(blank=True, to='seasons.Season', null=True),
            preserve_default=True,
        ),
    ]
