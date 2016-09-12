import csv
import sys

from ebisc.celllines.models import Cellline, CelllineBatch


'''Export CSV with batch IDs'''


# -----------------------------------------------------------------------------
#  Run

def run():

    writer = csv.writer(sys.stdout, dialect=csv.excel_tab, delimiter=',')

    writer.writerow((
        'cell_line_name',
        'cell_line_biosamples_id',
        'batch_no',
        'batch_biosamples_id',
        'batch_type',
    ))

    for batch in CelllineBatch.objects.all().order_by('cell_line__name'):

        writer.writerow((
            batch.cell_line.name,
            batch.cell_line.biosamples_id,
            batch.batch_id,
            batch.biosamples_id,
            batch.batch_type,
        ))

# -----------------------------------------------------------------------------
