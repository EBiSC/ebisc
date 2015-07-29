from django_docopt_command import DocOptCommand

import logging
logger = logging.getLogger('management.commands')

from django.core.management.base import CommandError

from ebisc.celllines import importer
from ebisc.celllines.models import *


DOCS = '''
Usage:
  import hotstart [--init] <directory>
  import lims
  import batches <filename>
  import toelastic
'''


class Command(DocOptCommand):

    docs = DOCS
    help = 'EBISC data importer'

    def handle_docopt(self, args):

        if args.get('hotstart'):

            if args.get('--init'):
                logger.info('Initializing database')
                for model in [Disease, Celltype, Celllineorgtype, Organization, Cellline, NonIntegratingVector]:
                    model.objects.all().delete()

            importer.hotstart.run(args.get('<directory>'))

        if args.get('lims'):
            importer.lims.run()

        if args.get('batches'):
            importer.batches.run(args.get('<filename>'))

        if args.get('toelastic'):
            importer.toelastic.run()
