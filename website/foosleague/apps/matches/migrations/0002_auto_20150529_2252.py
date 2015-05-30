# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(verbose_name='Season', blank=True, to='seasons.Season', null=True),
            preserve_default=True,
        ),
    ]
