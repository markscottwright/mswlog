# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weighin',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='weighin',
            name='pounds',
            field=models.FloatField(default=0),
        ),
    ]
