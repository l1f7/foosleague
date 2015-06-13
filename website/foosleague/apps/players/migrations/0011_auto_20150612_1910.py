# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0003_season_league'),
        ('matches', '0004_match_league'),
        ('players', '0010_auto_20150603_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('ts_mu', models.FloatField(default=25, help_text=b'higher the better', verbose_name='TrueSkill')),
                ('ts_sigma', models.FloatField(default=8.3333, help_text=b'Basically an indicator of accuracy', verbose_name='TrueSKill')),
                ('season_points', models.IntegerField(default=0, verbose_name='Season Points')),
                ('notes', models.TextField(default=b'', verbose_name='Notes')),
                ('match', models.ForeignKey(to='matches.Match', blank=True)),
                ('player', models.ForeignKey(to='players.Player')),
                ('season', models.ForeignKey(to='seasons.Season', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Stat History',
                'verbose_name_plural': 'Stat Histories',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('-ts_mu',), 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
    ]
