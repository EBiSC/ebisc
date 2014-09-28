from base import *

DEBUG = False
TEMPLATE_DEBUG = False

EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'eBisc <www@sevenpastnine.com>'

ALLOWED_HOSTS = ['ebisc.at.two.sevenpastnine.com']

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': 'www',
        'HOST': 'db',
    }
}

# -----------------------------------------------------------------------------
# Performance optimizations

USE_ETAGS = True

# -----------------------------------------------------------------------------
# Django static assets compressor

COMPRESS_OFFLINE = True

# -----------------------------------------------------------------------------
