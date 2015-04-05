# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
import django.contrib.postgres.fields
import markitup.fields


class Migration(migrations.Migration):

    replaces = [('articles', '0001_squashed_0004_auto_20150201_1335'), ('articles', '0002_auto_20150405_1650')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='slug')),
                ('content', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='content')),
                ('_content_rendered', models.TextField(editable=False, blank=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), default=[], size=None, blank=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
