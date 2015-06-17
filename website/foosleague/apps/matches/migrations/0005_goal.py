# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150610_1031'),
        ('matches', '0004_match_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('value', models.FloatField(default=1, help_text=b'corrections will be stored as -1', verbose_name='Value')),
                ('raspberry_pi', models.BooleanField(default=False)),
                ('match', models.ForeignKey(to='matches.Match')),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
            bases=(models.Model,),
        ),
    ]
