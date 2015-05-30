# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_trueskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('photo', models.ImageField(upload_to=b'leagues', max_length=250, verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'League',
                'verbose_name_plural': 'Leagues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LeagueMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('league', models.ForeignKey(verbose_name='League', to='leagues.League')),
                ('player', models.ForeignKey(verbose_name='Player', to='players.Player')),
            ],
            options={
                'verbose_name': 'League Member',
                'verbose_name_plural': 'League Members',
            },
            bases=(models.Model,),
        ),
    ]
