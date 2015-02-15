# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
import markitup.fields
import django.utils.timezone
import model_utils.fields

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='slug')),
                ('content', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='content')),
                ('_content_rendered', models.TextField(editable=False, blank=True)),
                ('tags', djorm_pgarray.fields.TextArrayField(dbtype='text')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
    ]
