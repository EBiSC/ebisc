from .base import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['cells.ebisc.org', 'cell.ebisc.org', 'catalog.ebisc.org', 'catalogue.ebisc.org', 'ebisc.douglasconnect.com', '193.62.54.96', '127.0.0.1']

SERVER_EMAIL = 'EBiSC <www@douglasconnect.com>'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

BIOSAMPLES_ADMINS = ADMINS + (
#    ('Biosamples', 'biosamples@ebi.ac.uk'),
)

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
    'url': 'http://www.ebi.ac.uk/biosamples',
    'key': os.getenv('BIOSAMPLES_KEY'),
}

# -----------------------------------------------------------------------------
