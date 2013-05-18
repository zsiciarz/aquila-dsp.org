# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2013.

from django.contrib import sitemaps

from .models import Article


class ArticleSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.modified
