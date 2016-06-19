# Copyright (c) Zbigniew Siciarz 2010-2016.

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap as django_sitemap
from django.views.generic import TemplateView

from . import views
from .sitemaps import StaticSitemap
from articles.sitemaps import ArticleSitemap

admin.autodiscover()

sitemaps = {
    'pages': StaticSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    url(
        regex=r'^$',
        view=views.main,
        name='main'
    ),
    url(
        regex=r'^about/$',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    url(
        regex=r'^features/$',
        view=TemplateView.as_view(template_name='features.html'),
        name='features'
    ),
    url(
        regex=r'^docs/$',
        view=TemplateView.as_view(template_name='docs.html'),
        name='docs'
    ),
    url(
        regex=r'^download/$',
        view=TemplateView.as_view(template_name='download.html'),
        name='download'
    ),
    url(
        regex=r'^dev/$',
        view=TemplateView.as_view(template_name='dev.html'),
        name='dev'
    ),
    url(
        regex=r'^license/$',
        view=TemplateView.as_view(template_name='license.html'),
        name='license'
    ),
    url(
        regex=r'^sitemap/$',
        view=views.sitemap,
        name='sitemap'
    ),
    url(
        regex=r'^examples/(?P<slug>[-\w]+)/$',
        view=views.RedirectExamplesView.as_view()
    ),
    url(
        regex=r'^sitemap\.xml$',
        view=django_sitemap,
        kwargs={
            'sitemaps': sitemaps,
        }
    ),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^markitup/', include('markitup.urls')),
]
