# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(default=b'', max_length=250, verbose_name='Name', blank=True)),
                ('logo', models.ImageField(default=b'', upload_to=b'logos', max_length=500, verbose_name='Logo', blank=True)),
                ('player_1', models.ForeignKey(related_name='player_1', verbose_name='Player 1', to='players.Player')),
                ('player_2', models.ForeignKey(related_name='player_2', verbose_name='Player 2', to='players.Player')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
