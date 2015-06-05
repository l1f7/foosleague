# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20150529_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='subdomain',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'name', verbose_name='subdomain', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
