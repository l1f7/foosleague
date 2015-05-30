# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(default=b'', help_text=b'Season Name', max_length=250, verbose_name='Name')),
                ('start', models.DateField(verbose_name='Season Start')),
                ('end', models.DateField(verbose_name='Season End')),
            ],
            options={
                'verbose_name': 'Seasons',
            },
            bases=(models.Model,),
        ),
    ]
