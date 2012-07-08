# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

u"""
Article syndication feeds.
"""

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

from .models import Article


class ArticleFeed(Feed):
    u"""
    RSS feed with latest articles.
    """

    title = _(u"aquila-dsp.org - articles")
    link = reverse_lazy('articles-article_list')
    description = _(u"News and information about Aquila DSP library.")

    def items(self):
        u"""
        Returns recent articles.
        """
        return Article.objects.all()[:5]

    def item_title(self, item):
        u"""
        Returns the title of a given article.
        """
        return item.title

    def item_description(self, item):
        u"""
        Returns the HTML content of a given article as the items description.
        """
        return item.content
