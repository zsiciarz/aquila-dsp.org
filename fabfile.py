# -*- coding: utf-8 -*-

from contextlib import nested

from fabric.api import *


def prepare_project():
    u"""
    Enters the directory and sources environment configuration.

    I know ``nested`` is deprecated, but what a nice shortcut it is here ;)
    """
    return nested(
        cd(PROJECT_PATH),
        prefix("source ../bin/activate"),
        prefix("source ./aquila/.environment")
    )


PROJECT_PATH = "$HOME/v/aquila-dsp.org/aquila-dsp.org"

env.roledefs = {
    'web': ["siciarz@siciarz.megiteam.pl"],
}
env.color = True


@task
@roles("web")
def git_pull():
    with cd(PROJECT_PATH):
        run("git pull origin master")


@task
@roles("web")
def update_requirements():
    with prepare_project():
        run("pip install -r requirements.txt")


@task
@roles("web")
def migrate():
    with prepare_project():
        run("python manage.py syncdb")
        run("python manage.py migrate")


@task
@roles("web")
def collect_static():
    with prepare_project():
        run("python manage.py collectstatic --noinput")


@task
@roles("web")
def restart():
    run("appctl restart aquila-dsp.org")


@task
def open_browser():
    import webbrowser
    webbrowser.open("http://aquila-dsp.org")


@task
@roles("web")
def deploy():
    git_pull()
    update_requirements()
    migrate()
    collect_static()
    restart()
