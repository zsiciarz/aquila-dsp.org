# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150201_1303'),
    ]

    operations = [
        migrations.RenameField('article', 'new_tags', 'tags'),
    ]
