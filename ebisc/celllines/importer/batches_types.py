import csv

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import CelllineBatch


'''Batch type importer'''


# -----------------------------------------------------------------------------
#  Run

def run(filename):

    with open(filename, 'rU') as csvfile:

        reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=',')

        next(reader, None)

        for row in reader:

            (_, _, _, _, cell_line_biosamples_id, batch_id, batch_biosamples_id, batch_type, _, _, _, _, _) = row

            try:
                if batch_biosamples_id:
                    batch = CelllineBatch.objects.get(biosamples_id=batch_biosamples_id)
                else:
                    batch = CelllineBatch.objects.get(cell_line__biosamples_id=cell_line_biosamples_id)

                if batch_type:
                    batch.batch_type = batch_type
                else:
                    batch.batch_type = 'unknown'
                batch.save()

            except CelllineBatch.DoesNotExist:
                logger.warn('Cell line batch with biosamples ID {} does not exists'.format(batch_biosamples_id))
                pass


# -----------------------------------------------------------------------------
