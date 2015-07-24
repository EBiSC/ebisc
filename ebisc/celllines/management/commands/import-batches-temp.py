import csv

from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from ...models import Cellline, CelllineBatch, CelllineAliquot

import logging
logger = logging.getLogger('management.commands')


class Command(BaseCommand):

    args = '<file>'
    help = 'Import cell line batch and vial biosamples IDs'

    def handle(self, *args, **options):

        filename = args[0]

        with open(filename, 'rb') as csvfile:

            reader = csv.reader(csvfile, delimiter='\t')

            next(reader, None)

            for row in reader:

                (vial_biosamples_id, _, _, cellline_biosamples_id, _, _, _, _, batch_biosamples_id) = row

                try:
                    cellline = Cellline.objects.get(biosamplesid=cellline_biosamples_id)
                    batch = self.create_batch(cellline, batch_biosamples_id)
                    aliquot = self.create_aliquot(batch, vial_biosamples_id)

                    logger.info('Created cell line %s, batch %s, aliquot %s' % (cellline, batch, aliquot))

                except Cellline.DoesNotExist:
                    pass
                    # logger.warn('Cell line with biosamples ID %s does not exists' % cellline_biosamples_id)

    def create_batch(self, cellline, batch_biosamples_id):

        batch, created = CelllineBatch.objects.get_or_create(
            cell_line=cellline,
            batch_id=batch_biosamples_id,
            biosamplesid=batch_biosamples_id,
        )

        return batch

    def create_aliquot(self, batch, aliquot_biosamples_id):

        aliquot, created = CelllineAliquot.objects.get_or_create(
            batch=batch,
            biosamplesid=aliquot_biosamples_id,
        )

        return aliquot
