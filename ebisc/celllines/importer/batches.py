import csv

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import Cellline, CelllineBatch, CelllineAliquot


'''Batch and vial biosamples IDs importer'''


# -----------------------------------------------------------------------------
#  Run

def run(filename):

    # with open(filename, 'rb') as csvfile:
    with open(filename, 'rU') as csvfile:

        # TODO combine files
        # reader = csv.reader(csvfile, delimiter='\t')
        # reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=',')
        reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter='\t')

        next(reader, None)

        for row in reader:

            (vial_biosamples_id, vial_name, _, cellline_biosamples_id, _, _, _, _, batch_biosamples_id) = row

            try:
                cell_line = Cellline.objects.get(biosamples_id=cellline_biosamples_id)
                batch = create_batch(cell_line, batch_biosamples_id)
                create_aliquot(batch, vial_biosamples_id, vial_name)

            except Cellline.DoesNotExist:
                pass
                # logger.warn('Cell line with biosamples ID %s does not exists' % cellline_biosamples_id)


# -----------------------------------------------------------------------------
#  Utils

def create_batch(cell_line, batch_biosamples_id):

    try:
        batch = CelllineBatch.objects.get(cell_line=cell_line, biosamples_id=batch_biosamples_id)

        return batch

    except CelllineBatch.DoesNotExist:
        batch = CelllineBatch(
            cell_line=cell_line,
            batch_id=batch_biosamples_id,  # temporarily use batch_biosamples_id
            biosamples_id=batch_biosamples_id,
        )

        batch.save()

        logger.info('Created batch {} for cell line {}'.format(batch, cell_line))
        return batch


def create_aliquot(batch, aliquot_biosamples_id, aliquot_name):

    aliquot, created = CelllineAliquot.objects.get_or_create(
        batch=batch,
        biosamples_id=aliquot_biosamples_id,
    )

    aliquot.name = aliquot_name

    aliquot.save()

    if created:
        logger.info('Created aliquot {} for cell line {} and batch {}'.format(aliquot, batch.cell_line, batch))

    return aliquot

# -----------------------------------------------------------------------------
