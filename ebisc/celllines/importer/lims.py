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

    for lims_batch in query(settings.LIMS.get('url')):

        logger.info('Processing batch {} for cell line {}'.format(lims_batch.batch_id, lims_batch.cell_line))

        lims_batch_data = query(lims_batch.href)

        if not lims_batch_data.biosamples_batch_id:
            logger.warn('Missing biosamples ID ... skipping batch')
            continue

        try:
            batch = CelllineBatch.objects.get(biosamples_id=lims_batch_data.biosamples_batch_id)

            batch.batch_id = lims_batch_data.batch_id
            # batch.passage_number = lims_batch_data.passage_number
            # batch.cells_per_vial = lims_batch_data.cells_per_vial
            batch.save()

            batch.cell_line.ecacc_id = lims_batch_data.ecacc_cat_no
            batch.cell_line.save()

        except CelllineBatch.DoesNotExist:
            logger.warn('Unknown batch with biosamples ID = {}'.format(lims_batch_data.biosamples_batch_id))


# -----------------------------------------------------------------------------
#  Utils

def query(url):
    return ToObject(requests.get(url, auth=(settings.LIMS.get('username'), settings.LIMS.get('password'))).json()).data

# -----------------------------------------------------------------------------
