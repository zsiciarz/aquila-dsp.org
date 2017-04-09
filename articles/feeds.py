# Copyright (c) Zbigniew Siciarz 2010-2016.

"""
Article syndication feeds.
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _

from .models import Article


class ArticleFeed(Feed):
    """
    RSS feed with latest articles.
    """

    title = _("aquila-dsp.org - articles")
    link = reverse_lazy('articles-article_list')
    description = _("News and information about Aquila DSP library.")

    def items(self):
        """
        Returns recent articles.
        """
        return Article.objects.all()[:5]

    def item_title(self, item):
        """
        Returns the title of a given article.
        """
        return item.title

    def item_description(self, item):
        """
        Returns the HTML content of a given article as the items description.
        """
        return item.content
