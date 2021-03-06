# Copyright (c) Zbigniew Siciarz 2010-2016.

import re
from django import template


register = template.Library()


@register.simple_tag
def active_tab(request, pattern):
    if re.search(pattern, request.path):
        return 'selected'
    return ''
