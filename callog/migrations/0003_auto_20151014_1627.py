# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callog', '0002_auto_20151011_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighin',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
