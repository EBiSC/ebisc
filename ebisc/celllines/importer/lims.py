import requests
from easydict import EasyDict as ToObject

import logging
logger = logging.getLogger('management.commands')

from django.conf import settings

from ebisc.celllines.models import Cellline, CelllineBatch, BatchCultureConditions


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
            batch.vials_at_roslin = value_of_int(lims_batch_data.vials_at_roslin)
            batch.vials_shipped_to_ecacc = value_of_int(lims_batch_data.vials_shipped_to_ECACC)
            batch.vials_shipped_to_fraunhoffer = value_of_int(lims_batch_data.vials_shipped_to_fraunhoffer)
            batch.save()

            culture_conditions, created = BatchCultureConditions.objects.get_or_create(batch=batch)
            if created:
                logger.info('Created new batch culture conditions')

            culture_conditions.culture_medium = lims_batch_data.culture_conditions.medium
            culture_conditions.matrix = lims_batch_data.culture_conditions.matrix
            culture_conditions.passage_method = lims_batch_data.culture_conditions.passage_method
            culture_conditions.o2_concentration = lims_batch_data.culture_conditions.O2_concentration
            culture_conditions.co2_concentration = lims_batch_data.culture_conditions.CO2_concentration
            culture_conditions.temperature = lims_batch_data.culture_conditions.temperature
            culture_conditions.save()

            batch.cell_line.ecacc_id = lims_batch_data.ecacc_cat_no
            batch.cell_line.save()

        except CelllineBatch.DoesNotExist:
            logger.warn('Unknown batch with biosamples ID = {}'.format(lims_batch_data.biosamples_batch_id))


# -----------------------------------------------------------------------------
#  Utils

def query(url):
    return ToObject(requests.get(url, auth=(settings.LIMS.get('username'), settings.LIMS.get('password'))).json()).data


def value_of_int(value):
    if value != '':
        return value
    else:
        return None

# -----------------------------------------------------------------------------
