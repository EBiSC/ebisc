import os
import datetime
from contextlib import contextmanager as context

from fabric.api import env, task, local, cd, run, prefix, get, settings
from fabric.contrib.project import rsync_project

SLUG = 'ebisc'
STORAGE = 'var/media/'
DESTDIR = '/var/projects/%s/' % SLUG

env.port = 65022
env.forward_agent = True
env.shell = '/bin/sh -c'
env.activate = '. %s/var/virtualenv/bin/activate' % DESTDIR

env.roledefs = {
    'production': ['www@cells.ebisc.org'],
    'staging': ['www@cells-stage.ebisc.org'],
}


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
        run('pip install pip --upgrade')
        run('pip install -r requirements.txt --upgrade')
        run('./manage.py migrate')
        run('./manage.py collectstatic --noinput')
        run('touch etc/conf/*.ini')


# -----------------------------------------------------------------------------
# Import data

@task
def update():

    with virtualenv():
        run('./manage.py import all')


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

    run('pg_dump %s | gzip -c > %s' % (SLUG, fn))
    get(fn, fn)

    with settings(warn_only=True):
        local('dropdb %s' % SLUG)
    local('createdb %s' % SLUG)

    run('rm %s' % fn)

    local('gunzip -c %s | psql -f - %s' % (fn, SLUG))
    local('rm %s' % fn)


# -----------------------------------------------------------------------------
# Model visualizations

@task
def visualize_model(group, layout='dot'):

    input_file = 'etc/mviz/%s.txt' % group

    output_dir = 'var/mviz'
    output_file = '%s/%s.png' % (output_dir, group)

    header_bgcolor = '#1b85cfff'
    body_bgcolor = '#efefef'

    local('mkdir -p %s' % output_dir)
    # local('./manage.py graph_models celllines --disable-fields --verbose-names --include-models=%s | sed s/BGCOLOR=\\"olivedrab4\\"/BGCOLOR=\\"%s\\"/g | sed s/BGCOLOR=\\"palegoldenrod\\"/BGCOLOR=\\"%s\\"/g | %s -Tpng -o %s' % (input_file, header_bgcolor, body_bgcolor, layout, output_file))
    local('./manage.py graph_models celllines --verbose-names --include-models=%s | sed s/BGCOLOR=\\"olivedrab4\\"/BGCOLOR=\\"%s\\"/g | sed s/BGCOLOR=\\"palegoldenrod\\"/BGCOLOR=\\"%s\\"/g | %s -Tpng -o %s' % (input_file, header_bgcolor, body_bgcolor, layout, output_file))

# -----------------------------------------------------------------------------
