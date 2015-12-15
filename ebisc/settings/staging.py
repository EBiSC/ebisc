from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['cells-stage.ebisc.org']

SERVER_EMAIL = 'EBiSC Staging <www@douglasconnect.com>'

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': 'www',
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': 'localhost', 'port': 9200}]

# -----------------------------------------------------------------------------
