from .base import *
import os

DEBUG = False

IS_LIVE = False

ALLOWED_HOSTS = ['ebisc-ims.charite.de']

BIOSAMPLES_ADMINS = ADMINS

# write (error) mails to console on mail server problems:
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'ebisc'),
        'USER': os.getenv('DB_USER', 'www'),
        'PASSWORD': os.getenv('DB_PASS', None),
        'HOST': os.getenv('DB_HOST', None),
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': os.getenv('ES_HOST', 'localhost'), 'port': 9200}]

# -----------------------------------------------------------------------------
