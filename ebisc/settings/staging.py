from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ebisc-stage.douglasconnect.com']

SERVER_EMAIL = 'EBiSC Staging <joh@douglasconnect.com>'

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
