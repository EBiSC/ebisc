import csv
import re

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import Cellline, CelllineBatch


'''Batch type importer'''


# -----------------------------------------------------------------------------
#  Run

def run(filename):

    with open(filename, 'rU') as csvfile:

        reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter='\t')

        next(reader, None)

        for row in reader:

            (cell_line_name, cell_line_biosamples_id, batch_no, batch_biosamples_id, batch_type, batch_type_slug) = row

            try:
                batch = CelllineBatch.objects.get(biosamples_id=batch_biosamples_id)
                batch.batch_type = batch_type_slug
                print batch.batch_type
                batch.save()

            except CelllineBatch.DoesNotExist:
                pass


# -----------------------------------------------------------------------------
