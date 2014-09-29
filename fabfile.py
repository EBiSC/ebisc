import datetime
from contextlib import contextmanager as context

from fabric.api import *

SLUG = 'ebisc'
DJANGO = '1.7'
STORAGE = 'var/media/'
DESTDIR = '/var/projects/%s' % SLUG

env.hosts = ['www@django.two.sevenpastnine.com']
env.port = 65022
env.forward_agent = True
# env.shell = '/usr/local/bin/bash -l -c'
env.shell = '/bin/sh -c'
env.activate = '. /usr/local/virtualenv/django-%s/bin/activate' % DJANGO


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
        # run('bower install')
        run('./manage.py collectstatic --noinput')
        run('./manage.py compress')
        run('touch etc/conf/staging.uwsgi.ini')


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
    local('rsync -avH %s:%s/%s %s' % (env.host_string, DESTDIR, STORAGE, STORAGE))


def sync_db():

    fn = '%s-%s.sql.bz2' % (SLUG, str(datetime.datetime.now()).replace(' ', '-'))

    run('pg_dump -h db %s | bzip2 -c > %s' % (SLUG, fn))
    get(fn, fn)

    with settings(warn_only=True):
        local('dropdb %s' % SLUG)
    local('createdb %s' % SLUG)

    run('rm %s' % fn)

    local('bunzip2 -c %s | psql -f - %s' % (fn, SLUG))
    local('rm %s' % fn)

# -----------------------------------------------------------------------------
