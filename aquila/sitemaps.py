# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2013.

from django.contrib import sitemaps


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['news', 'about', 'features', 'docs', 'download', 'dev', 'license']

    def location(self, obj):
        return '/%s/' % obj
