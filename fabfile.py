import os
import datetime
from contextlib import contextmanager as context

from fabric.api import env, task, local, cd, run, prefix, get, settings
from fabric.contrib.project import rsync_project

SLUG = 'ebisc'
STORAGE = 'var/media/'
DESTDIR = '/var/projects/%s/' % SLUG

env.hosts = ['www@django.two.sevenpastnine.com']
env.port = 65022
env.forward_agent = True
env.shell = '/bin/sh -c'
env.activate = '. %s/var/virtualenv/bin/activate' % DESTDIR


# -----------------------------------------------------------------------------
# Virtualenv

@context
def virtualenv():
    with cd(DESTDIR):
        with prefix(env.activate):
            yield


# -----------------------------------------------------------------------------
# Deploy

@task
def deploy(option=None):

    with virtualenv():
        run('git pull origin')
        run('bower install --production')
        run('pip install -r requirements.txt')
        run('./manage.py collectstatic --noinput')
        run('touch etc/conf/*.ini')


# -----------------------------------------------------------------------------
# Sync

@task
def sync(kind=None):
    if kind == 'db':
        sync_db()
    elif kind == 'media':
        sync_media()
    else:
        sync_db()
        sync_media()


def sync_media():
    rsync_project(os.path.join(DESTDIR, STORAGE), STORAGE, upload=False)


def sync_db():
    fn = '%s-%s.sql.gz' % (SLUG, str(datetime.datetime.now()).replace(' ', '-'))

    run('pg_dump -h db %s | gzip -c > %s' % (SLUG, fn))
    get(fn, fn)

    with settings(warn_only=True):
        local('dropdb %s' % SLUG)
    local('createdb %s' % SLUG)

    run('rm %s' % fn)

    local('gunzip -c %s | psql -f - %s' % (fn, SLUG))
    local('rm %s' % fn)


# -----------------------------------------------------------------------------
