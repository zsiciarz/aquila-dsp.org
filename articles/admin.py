# Copyright (c) Zbigniew Siciarz 2010-2016.

"""
Administration for articles.
"""

from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    Administration for articles.
    """

    list_display = ['title', 'slug', 'created', 'modified']
    list_filter = ['created']
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
