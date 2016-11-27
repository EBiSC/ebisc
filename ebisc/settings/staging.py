from .base import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['cells-stage.ebisc.org']

SERVER_EMAIL = 'EBiSC Staging <www@douglasconnect.com>'

BIOSAMPLES_ADMINS = ADMINS

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': os.getenv('DB_USER', 'www'),
        'PASSWORD': os.getenv('DB_PASS', None),
        'HOST': os.getenv('DB_HOST', None),
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': os.getenv('ES_HOST', 'localhost'), 'port': 9200}]

# -----------------------------------------------------------------------------
