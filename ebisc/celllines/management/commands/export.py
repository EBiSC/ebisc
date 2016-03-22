from django_docopt_command import DocOptCommand

import logging
logger = logging.getLogger('management.commands')

from django.core.management.base import CommandError

from ebisc.celllines import exporter


DOCS = '''
Usage:
  export ecacc
  export batches
'''


class Command(DocOptCommand):

    docs = DOCS
    help = 'EBISC data exporter'

    def handle_docopt(self, args):

        if args.get('ecacc'):
            exporter.ecacc.run()

        if args.get('batches'):
            logger.info('Exporting batches')
            exporter.batches.run()
