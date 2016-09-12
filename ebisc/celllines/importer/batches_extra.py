import csv
import re

import logging
logger = logging.getLogger('management.commands')

from django.db import IntegrityError

from ebisc.celllines.importer.hpscreg.utils import format_integrity_error

from ebisc.celllines.models import Cellline, CelllineBatch, CelllineAliquot


'''Batch and vial biosamples IDs importer for extra, incomplete batch data'''


# -----------------------------------------------------------------------------
#  Run

def run(filename):

    with open(filename, 'rU') as csvfile:

        reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=',')

        next(reader, None)

        for row in reader:

            # (vial_biosamples_id, vial_name, _, cellline_biosamples_id, _, _, _, _, batch_biosamples_id) = row
            (vial_biosamples_id, vial_name_old, vial_name, _, _, cellline_biosamples_id, _, _, _, _, _, _, batch_biosamples_id, _, batch_name, _, _) = row

            extra_lines_with_complete_data = ['SAMEA4096428', 'SAMEA4309665']

            if vial_name and cellline_biosamples_id not in extra_lines_with_complete_data:
                logger.info('Skipping complete batch {} for cell line {}'.format(batch_name, cellline_biosamples_id))
            else:
                if batch_name:
                    try:
                        cell_line = Cellline.objects.get(biosamples_id=cellline_biosamples_id)
                        batch = create_batch(cell_line, batch_biosamples_id, batch_name)
                        create_aliquot(cell_line, batch, vial_biosamples_id, vial_name_old)

                    except Cellline.DoesNotExist:
                        pass
                        logger.warn('Cell line with biosamples ID %s does not exists' % cellline_biosamples_id)
                else:
                    pass


# -----------------------------------------------------------------------------
#  Utils

def create_batch(cell_line, batch_biosamples_id, batch_name):

    if batch_name:
        batch_id = re.split('[\s]+', batch_name)[-1]
    else:
        # temporarily use batch_biosamples_id if batch name is not available
        batch_id = batch_biosamples_id

    try:
        batch, created = CelllineBatch.objects.update_or_create(
            cell_line=cell_line,
            biosamples_id=batch_biosamples_id,
            defaults={
                'batch_id': batch_id,
            }
        )

        if created:
            logger.info('Created batch {} for cell line {}'.format(batch, cell_line))

        return batch

    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None


def create_aliquot(cell_line, batch, aliquot_biosamples_id, aliquot_name_old):

    aliquot_number = re.split('[\s]+', aliquot_name_old)[-1]
    aliquot_number = aliquot_number.zfill(4)

    aliquot_name = '%s %s vial %s' % (cell_line.name, batch.batch_id, aliquot_number)

    try:
        aliquot, created = CelllineAliquot.objects.update_or_create(
            batch=batch,
            biosamples_id=aliquot_biosamples_id,
            defaults={
                'name': aliquot_name,
                'number': aliquot_number,
            }
        )

        if created:
            logger.info('Created aliquot {} for cell line {} and batch {}'.format(aliquot, batch.cell_line, batch))

        return aliquot

    except IntegrityError, e:
        logger.warn(format_integrity_error(e))
        return None

# -----------------------------------------------------------------------------
