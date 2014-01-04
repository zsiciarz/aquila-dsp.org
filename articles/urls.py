# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2014.

from django.conf.urls import patterns, url

from .feeds import ArticleFeed
from .views import ArticleListView, TaggedArticleListView, ExampleListView, \
    ArticleDetailsView


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ArticleListView.as_view(),
        name='articles-article_list'
    ),
    url(
        regex=r'^tag/(?P<tag>[\w\+]+)/$',
        view=TaggedArticleListView.as_view(),
        name='articles-tagged_article_list'
    ),
    url(
        regex=r'^examples/$',
        view=ExampleListView.as_view(),
        name='articles-example_list'
    ),
    url(
        regex=r'^rss/$',
        view=ArticleFeed(),
        name='articles-rss'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ArticleDetailsView.as_view(),
        name='articles-article_details'
    ),
)
