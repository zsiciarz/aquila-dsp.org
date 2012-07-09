# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import RedirectView

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


class RedirectExamplesView(RedirectView):
    permanent = True

    def get_redirect_url(self, slug):
        return reverse('articles-article_details', args=[], kwargs={'slug': slug})
