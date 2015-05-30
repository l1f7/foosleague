# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('team_1_score', models.IntegerField(default=0, verbose_name='Team 1 Score')),
                ('team_2_score', models.IntegerField(default=0, verbose_name='Team 2 Score')),
                ('team_1', models.ForeignKey(related_name='team_1', to='teams.Team')),
                ('team_2', models.ForeignKey(related_name='team_2', to='teams.Team')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
            bases=(models.Model,),
        ),
    ]
