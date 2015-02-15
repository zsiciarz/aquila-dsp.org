# Copyright (c) Zbigniew Siciarz 2010-2015.

from django import template

from github import Github


register = template.Library()


@register.inclusion_tag("commit.html")
def last_commit(username, repository_name):
    """
    Returns last Git commit for a given repository.
    """
    try:
        g = Github()
        user = g.get_user(username)
        repo = user.get_repo(repository_name)
        commits = repo.get_commits()
        return {'commit': commits[0]}
    except Exception:
        return {'commit': None}
