from .base import *
import os

DEBUG = False

IS_LIVE = True

ALLOWED_HOSTS = ['cells.ebisc.org', 'cell.ebisc.org', 'catalog.ebisc.org', 'catalogue.ebisc.org', 'ebisc-ims.charite.de', 'ebisc-ims.cell-type.org', '127.0.0.1', '141.42.207.1', 'cells-stage.ebisc.org']

BIOSAMPLES_ADMINS = ADMINS + (
   ('Biosamples', 'biosamples@ebi.ac.uk'),
)

# write (error) mails to console on mail server problems:
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'ebisc'),
        'USER': os.getenv('DB_USER', 'www'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': os.getenv('ES_HOST', 'localhost'), 'port': 9200}]

# -----------------------------------------------------------------------------
# BioSamples

BIOSAMPLES = {
    'url': 'https://www.ebi.ac.uk/biosamples',
    'key': os.getenv('BIOSAMPLES_KEY'),
}

# -----------------------------------------------------------------------------
