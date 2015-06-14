# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_match_league'),
        ('players', '0016_auto_20150613_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExposeHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('expose', models.FloatField(default=0, help_text=b'leaderboard', verbose_name='TrueSkill Expose')),
                ('match', models.ForeignKey(to='matches.Match')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
