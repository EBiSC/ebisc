How to run IMS in docker
=======================

In the Embassy deployment, all components of IMS run in [docker](https://www.docker.com/) containers, i.e. postgres, elasticsearch, uwsgi, nginx etc.

For development, you can run the same containers on your local machine.
For development convenience, you can use [Docker compose](https://docs.docker.com/compose/) to easily start and stop the services. (but note we do not use docker-compose in production)

1. Postgres database
--------------------

Bring up the server

  docker-compose up -d postgres

Use this command if you want to start a client to poke around in the database. The password in development is ebisc.

  docker-compose run postgres psql -h ims-postgres -U www ebisc

To load the database for development, you need to get hold of a file "ebisc.sql.gz" by running pg_dump from the production instance.  Instructions for this are in a different repo.
Put the file "ebisc.sql.gz" in the same directory as the docker-compose file, and run this command:

  docker-compose run db_import

* We use the [openshift/postgresql-92-centos7](https://hub.docker.com/r/openshift/postgresql-92-centos7/) postgres image because it is production-ready and runs non-root.
* We use different passwords in production and development.

2. Elasticsearch
----------------

  docker-compose up -d elasticsearch

3. Django
----------

Create these sub-directories from the same directory as the docker-compose file:

  mkdir -p var/static var/media
  sudo chown 1001 var/static var/media

Bring up the uWSGI server:

  docker-compose up -d uwsgi

The stats socket is published to your local machine on port 9191.

  curl 127.0.0.1:9191

Run the deploy command. This runs the django commands
"migrate" and "collectstatic" which prepares the database and static files.

  docker-compose run deploy

Note, these instructions file builds a "develop" version of the uwsgi image which uses
the ebisc/settings/develop.py file. In production we use the ebisc/settings/production.py file.

4. nginx
--------

  docker-compose up -d nginx

This serves the app on port 8080 of your local machine. Open this link in your webrowser: [http://127.0.0.1:8080](http://127.0.0.1:8080)

The only thing you are missing now is "media" files, which are not part of this repo.
You will need to copy the latest "media" files from the production machine and put them in
your var/media directory.  This includes CofAs, cell images, instructions for depositors etc.

Principles of secure docker deployment
===============================

* All containers run non-root
* SELinux is enforced in production
* Drop all capabilities
* Only publish the important ports to localhost.
* Mount file systems read-only where possible.
* Use official docker repos, not user-contributed.  The only place where I broke this rule is the centos/postgres image.
* Keep passwords and API keys out of the image, in case the image ever accidentally ends up in a public repo.  Pass in passwords and keys at run time using environment variables.
* Run on a host with a minimal operating system. On Embassy we use coreos.

