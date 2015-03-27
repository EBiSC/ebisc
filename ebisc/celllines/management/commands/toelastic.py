import os
import json
from elasticsearch import Elasticsearch

import logging
logger = logging.getLogger('management.commands')

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Cellline

# -----------------------------------------------------------------------------
# Elasticsearch mappings and app schemas

BASEDIR = os.path.join(os.path.dirname(__file__), '../../elastic/')

MAPPINGS = {
    'cellline': os.path.abspath(os.path.join(BASEDIR, 'mappings/cellline.json'))
}


# -----------------------------------------------------------------------------
# Command

class Command(BaseCommand):

    help = 'Import ORM data to ElasticSearch.'

    def handle(self, *args, **options):

        es = Elasticsearch(settings.ELASTIC_HOSTS)

        # Create index

        logger.info(u'Creating ES index')
        es.indices.delete(index=settings.ELASTIC_INDEX, ignore=[404])
        es.indices.create(index=settings.ELASTIC_INDEX)

        # Create mappings

        logger.info(u'Creating mappings')
        with open(MAPPINGS['cellline']) as fi:
            for key, value in json.load(fi).items():
                logger.info(u'Creating mapping %s' % key)
                es.indices.put_mapping(index=settings.ELASTIC_INDEX, doc_type=key, body=value)

        # Import cell lines

        logger.info(u'Importing cell lines')
        for cellline in Cellline.objects.all():
            document = cellline.to_elastic()
            logger.debug(document)
            es.index(settings.ELASTIC_INDEX, doc_type='cellline', body=document)

# -----------------------------------------------------------------------------
