import csv

import logging
logger = logging.getLogger('management.commands')

from ebisc.celllines.models import Cellline


'''ECACC catalogue number importer'''


# -----------------------------------------------------------------------------
#  Run

def run(filename):

    with open(filename, 'rU') as csvfile:

        reader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=',')

        next(reader, None)

        for row in reader:

            (ecacc_cat_number, cell_line_name) = row

            try:
                cell_line = Cellline.objects.get(name=cell_line_name)

                if cell_line.ecacc_id:
                    if cell_line.ecacc_id == ecacc_cat_number:
                        logger.info('Numbers {} match for cell line {}'.format(cell_line.ecacc_id, cell_line.name))
                    else:
                        logger.warn('Numbers dont match for cell line {}, old: {}, new: {}'.format(cell_line.name, cell_line.ecacc_id, ecacc_cat_number))
                else:
                    logger.info('Found new ecacc num for line {}'.format(cell_line.name))
                    # cell_line.ecacc_id = ecacc_cat_number
                    # cell_line.save()

            except Cellline.DoesNotExist:
                logger.warn('Cell line with name {} does not exists'.format(cell_line_name))
                pass


# -----------------------------------------------------------------------------
