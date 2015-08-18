from django_docopt_command import DocOptCommand

from ebisc.celllines import importer
from ebisc.celllines.models import *

import logging
logger = logging.getLogger('management.commands')


DOCS = '''
Usage:
    import hpscreg [--init]
    import hotstart [--init] <directory>
    import lims
    import batches <filename>
    import toelastic
'''


class Command(DocOptCommand):

    docs = DOCS
    help = 'EBISC data importer'

    def handle_docopt(self, args):

        if args.get('hpscreg'):
            if args.get('--init'):
                self.init()
            importer.hpscreg.run()

        if args.get('hotstart'):
            if args.get('--init'):
                self.init()
            importer.hotstart.run(args.get('<directory>'))

        if args.get('lims'):
            logger.info('Synchronizing batch data with LIMS')
            importer.lims.run()

        if args.get('batches'):
            importer.batches.run(args.get('<filename>'))

        if args.get('toelastic'):
            importer.toelastic.run()

    def init(self):
        logger.info('Initializing database')
        for model in [Disease, Celltype, Celllineorgtype, Organization, Cellline, NonIntegratingVector]:
            model.objects.all().delete()
