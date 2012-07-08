# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailsView(DetailView):
    model = Article
