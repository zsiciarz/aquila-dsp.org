# Copyright (c) Zbigniew Siciarz 2010-2015.

from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article


class TaggedArticleListView(ArticleListView):
    def get_queryset(self):
        queryset = super(TaggedArticleListView, self).get_queryset()
        return queryset.filter(tags__contains=[self.kwargs['tag']])


class ExampleListView(ListView):
    queryset = Article.objects.filter(tags__contains=['example'])
    template_name = "articles/example_list.html"


class ArticleDetailsView(DetailView):
    model = Article
