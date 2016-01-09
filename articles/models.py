# Copyright (c) Zbigniew Siciarz 2010-2016.

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djorm_pgarray.fields import TextArrayField
from markitup.fields import MarkupField
from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    content = MarkupField(_("content"))

    tags = ArrayField(models.CharField(max_length=64), blank=True, default=[])

    class Meta:
        verbose_name_plural = _("Articles")
        ordering = ['-created']

    def __str__(self):
        """
        The string representation of an article is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles-article_details', [], {'slug': self.slug})
