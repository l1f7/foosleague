# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_remove_stathistory_ts_expose'),
        ('matches', '0008_auto_20150630_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='FanHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('fans', models.IntegerField(default=0)),
                ('match', models.ForeignKey(blank=True, to='matches.Match', null=True)),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
                'verbose_name': 'Fan History',
                'verbose_name_plural': 'Fan History',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FantasySetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('ticket_price', models.PositiveIntegerField(default=50)),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
                'verbose_name': 'Fantasy Setting',
                'verbose_name_plural': 'Fantasy Settings',
            },
            bases=(models.Model,),
        ),
    ]
