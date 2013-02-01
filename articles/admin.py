# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2013.

u"""
Administration for articles.
"""

from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    u"""
    Administration for articles.
    """

    list_display = ['title', 'slug', 'created', 'modified']
    list_filter = ['created']
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
