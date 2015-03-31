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
    ('Joh Dokler', 'joh.dokler@gmail.com'),
)

# -----------------------------------------------------------------------------
# Application definition

INSTALLED_APPS = (
    'ebisc',
    'ebisc.site',
    'ebisc.celllines',
    'ebisc.search',
    'ebisc.executive',

    'tastypie',
    'django_cleanup',
    'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
# Admin

from django.utils.translation import ugettext_lazy as _

GRAPPELLI_ADMIN_TITLE = _(u'EBiSC Administration')
GRAPPELLI_INDEX_DASHBOARD = 'ebisc.dashboard.CustomIndexDashboard'

# -----------------------------------------------------------------------------
# Authentication

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# -----------------------------------------------------------------------------
# Tastypie

TASTYPIE_ALLOW_MISSING_SLASH = True

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
