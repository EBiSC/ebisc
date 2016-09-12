from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['cells.ebisc.org', 'cell.ebisc.org', 'catalog.ebisc.org', 'catalogue.ebisc.org', 'ebisc.douglasconnect.com']

SERVER_EMAIL = 'EBiSC <www@douglasconnect.com>'

BIOSAMPLES_ADMINS = ADMINS + (
    ('Biosamples', 'biosamples@ebi.ac.uk'),
)

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': 'www',
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': 'localhost', 'port': 9200}]

# -----------------------------------------------------------------------------
# BioSamples

BIOSAMPLES = {
    'url': 'http://www.ebi.ac.uk/biosamples',
    'key': 'WNTGPBNW0NGC3876',
}

# -----------------------------------------------------------------------------
