from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ebisc.douglasconnect.com']

SERVER_EMAIL = 'EBiSC Staging <joh@douglasconnect.com>'

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': 'www',
        'HOST': 'db'
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': 'elastic', 'port': 9200}]

# -----------------------------------------------------------------------------
