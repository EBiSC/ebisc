from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

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

# -----------------------------------------------------------------------------