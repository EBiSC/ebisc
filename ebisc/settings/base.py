"""
Django settings for EBiSC project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY')

# -----------------------------------------------------------------------------
# Admins

ADMINS = (
    ('Peter Harrison', 'peter@ebi.ac.uk'),
    ('Luca Cherubin', 'cherubin@ebi.ac.uk'),
    ('Johannes Dewender', 'johannes.dewender@charite.de'),
    ('Trisha Rawat', 'Trisha.Rawat@phe.gov.uk'),
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # default
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # commented in default, but we want it
                'django.template.context_processors.request',
            ],
        },
    },
]

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
    'list_url': 'https://hpscreg.eu/api/export/ebisc',
    'local_list_url': '/get_data_export/?full=true',
    'cellline_url': 'https://hpscreg.eu/api/export/ebisc/',
    'local_cellline_url': '/get_data_export/?readable_values=true&ldap_user_id=' \
                          + os.getenv('HPSCREG_USER', 'ebiscims') + '&id=',
    'username': os.getenv('HPSCREG_USER', 'ebiscims'),
    'password': os.getenv('HPSCREG_PASSWORD'),
}

# -----------------------------------------------------------------------------
# LIMS

LIMS = {
    'url': 'http://www.ebi.ac.uk/~ebiscdcc/api/batch.json',
    'username': os.getenv('LIMS_USER'),
    'password': os.getenv('LIMS_PASSWORD'),
}

# -----------------------------------------------------------------------------
# BioSamples

BIOSAMPLES = {
    'url': 'https://wwwdev.ebi.ac.uk/biosamples',
    'key': os.getenv('BIOSAMPLES_KEY'),
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
