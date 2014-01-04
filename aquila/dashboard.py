# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2014.

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('AppList: Applications'),
            collapsible=False,
            column=1,
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('ModelList: Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
                {
                    'title': _('Translations'),
                    'url': reverse('rosetta.views.home'),
                    'external': False,
                },
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))

