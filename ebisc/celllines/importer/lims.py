import requests
from easydict import EasyDict as ToObject

import logging
logger = logging.getLogger('management.commands')

from django.conf import settings

from ebisc.celllines.models import Cellline, CelllineBatch


'''
LIMS batch data importer.
'''


# -----------------------------------------------------------------------------
#  Run

def run():

    logger.info('Synchronizing batch data with LIMS')

    for lims_batch in query(settings.LIMS.get('url')):

        logger.info('Processing batch {}'.format(lims_batch.batch_id))

        lims_batch_data = query(lims_batch.href)

        cell_line = Cellline.objects.get(celllinename=lims_batch_data.cell_line)

        batch, created = CelllineBatch.objects.get_or_create(
            cell_line=cell_line,
            biosamplesid=lims_batch_data.biosamples_batch_id
        )

        if created:
            logger.info('  Creating new batch {} for cell line {}'.format(batch, cell_line))
        else:
            logger.info('  Updating existing batch {} for cell line {}'.format(batch, cell_line))


# -----------------------------------------------------------------------------
#  Utils

def query(url):
    return ToObject(requests.get(url, auth=(settings.LIMS.get('username'), settings.LIMS.get('password'))).json()).data

# -----------------------------------------------------------------------------
