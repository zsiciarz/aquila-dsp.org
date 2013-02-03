# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2013.

from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article


class TaggedArticleListView(ArticleListView):
    def get_queryset(self):
        queryset = super(TaggedArticleListView, self).get_queryset()
        return queryset.filter(tags__name__in=[self.kwargs['tag']])


class ExampleListView(ListView):
    queryset = Article.objects.filter(tags__name__in=['example'])
    template_name = "articles/example_list.html"


class ArticleDetailsView(DetailView):
    model = Article
