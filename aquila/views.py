# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.shortcuts import render

from articles.models import Article


def main(request):
    articles = Article.objects.all()[:3]
    return render(request, 'index.html', {
        'articles': articles,
    })


def sitemap(request):
    articles = Article.objects.all()
    return render(request, 'sitemap.html', {
        'articles': articles,
    })
