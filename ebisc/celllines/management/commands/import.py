from django_docopt_command import DocOptCommand

from ebisc.celllines import importer
from ebisc.celllines.models import *

import logging
logger = logging.getLogger('management.commands')


DOCS = '''
Usage:
    import all [--traceback]
    import hpscreg [--traceback] [--cellline=<name>]
    import lims [--traceback]
    import batches [--traceback] <filename>
    import toelastic [--traceback]
'''


class Command(DocOptCommand):

    docs = DOCS
    help = 'EBISC data importer'

    def handle_docopt(self, args):

        if args.get('all'):
            importer.hpscreg.run()
            importer.lims.run()
            importer.toelastic.run()

        if args.get('hpscreg'):
            importer.hpscreg.run(cellline=args.get('--cellline'))

        if args.get('lims'):
            logger.info('Synchronizing batch data with LIMS')
            importer.lims.run()

        if args.get('toelastic'):
            importer.toelastic.run()

        if args.get('batches'):
            logger.info('Importing batches from BioSamples')
            importer.batches.run(args.get('<filename>'))
