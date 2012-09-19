# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.conf.urls import patterns, url

from .feeds import ArticleFeed
from .views import ArticleListView, ExampleListView, ArticleDetailsView


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ArticleListView.as_view(),
        name='articles-article_list'
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
