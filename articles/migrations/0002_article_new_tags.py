# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='new_tags',
            field=djorm_pgarray.fields.TextArrayField(dbtype='text'),
            preserve_default=True,
        ),
    ]
