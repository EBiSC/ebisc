from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INTERNAL_IPS = ['127.0.0.1']

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
    },
    # 'source': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'ebisc',
    # }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': 'localhost', 'port': 9200}]

# -----------------------------------------------------------------------------
