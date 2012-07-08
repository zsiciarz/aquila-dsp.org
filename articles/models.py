# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.db import models
from django.utils.translation import ugettext_lazy as _

from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(_(u"title"), max_length=255)
    slug = models.SlugField(_(u"slug"), max_length=255, unique=True)
    content = MarkupField(_(u"content"), default_markup_type='markdown')

    class Meta:
        verbose_name_plural = _(u"Articles")
        ordering = ['-created']

    def __unicode__(self):
        u"""
        The Unicode representation of an article is its title.
        """
        return self.title
