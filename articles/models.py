# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2014.

from django.db import models
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Article(TimeStampedModel):
    title = models.CharField(_(u"title"), max_length=255)
    slug = models.SlugField(_(u"slug"), max_length=255, unique=True)
    content = MarkupField(_(u"content"))

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = _(u"Articles")
        ordering = ['-created']

    def __unicode__(self):
        u"""
        The Unicode representation of an article is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles-article_details', [], {'slug': self.slug})
