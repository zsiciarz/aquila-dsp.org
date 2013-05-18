# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2013.

from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'about', 'features', 'docs', 'download', 'dev', 'license']

    def location(self, item):
        return reverse(item)
