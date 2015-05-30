# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20150529_2252'),
        ('players', '0005_auto_20150530_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('match', models.ForeignKey(to='matches.Match')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Bet',
                'verbose_name_plural': 'Bets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('bet', models.ForeignKey(blank=True, to='bookie.Bet', null=True)),
                ('match', models.ForeignKey(blank=True, to='matches.Match', help_text=b'Match will be linked, if transaction amount came from a win', null=True)),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
            bases=(models.Model,),
        ),
    ]
