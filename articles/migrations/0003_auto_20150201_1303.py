# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def copy_tags(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    ct = ContentType.objects.get(app_label='articles', model='article')
    print(ct)
    Article = apps.get_model('articles', 'Article')
    TaggedItem = apps.get_model('taggit', 'TaggedItem')
    for article in Article.objects.all():
        tags = TaggedItem.objects.filter(content_type=ct, object_id=article.pk).values_list('tag__name', flat=True)
        article.new_tags = tags
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_new_tags'),
    ]

    operations = [
            migrations.RunPython(copy_tags),
    ]
