"""
Django settings for EBiSC project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '@!7ju$b1*1c5!dihak)cw3ao1ema&2quw3s*9l#&8^v8ob%gw1'

# -----------------------------------------------------------------------------
# Admins & managers

ADMINS = (
    ('Joh Dokler', 'joh@douglasconnect.com'),
    ('Maja Brajnik', 'maja@douglasconnect.com'),
)

# -----------------------------------------------------------------------------
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ebisc',
    'ebisc.cms',
    'ebisc.site',
    'ebisc.celllines',
    'ebisc.executive',

    'tastypie',
    'django_cleanup',
    'sorl.thumbnail',
    'debug_toolbar',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ebisc.urls'

WSGI_APPLICATION = 'ebisc.wsgi.application'

# -----------------------------------------------------------------------------
# Internationalization

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'Europe/Paris'
USE_TZ = True

# -----------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../var/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../var/media/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# -----------------------------------------------------------------------------
# Templating

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# -----------------------------------------------------------------------------
# Authentication

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# -----------------------------------------------------------------------------
# Tastypie

TASTYPIE_DEFAULT_FORMATS = ['json']
TASTYPIE_ALLOW_MISSING_SLASH = True
API_LIMIT_PER_PAGE = 50

# -----------------------------------------------------------------------------
# Sorl thumbnails

THUMBNAIL_QUALITY = 80

# -----------------------------------------------------------------------------
# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)-10s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'management.commands': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# -----------------------------------------------------------------------------
# hPSCreg

HPSCREG = {
    'list_url': 'http://hpscreg.eu/api/full_list',
    'cellline_url': 'http://hpscreg.eu/api/export/',
    'username': 'ebiscims',
    'password': 'cWNJnc6p',
}

# -----------------------------------------------------------------------------
# LIMS

LIMS = {
    'url': 'http://www.ebi.ac.uk/~ebiscdcc/api/batch.json',
    'username': 'ebisc',
    'password': 'ebisc321',
}

# -----------------------------------------------------------------------------
# BioSamples

BIOSAMPLES = {
    'url': 'http://www.ebi.ac.uk/biosamples/beta',
    'key': 'WNTGPBNW0NGC3876',
}

# -----------------------------------------------------------------------------
# Markdown

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}

# -----------------------------------------------------------------------------
