# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_squashed_0004_auto_20150201_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, base_field=models.CharField(max_length=64), default=[]),
        ),
    ]
