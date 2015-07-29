from django_docopt_command import DocOptCommand

import logging
logger = logging.getLogger('management.commands')

from django.core.management.base import CommandError

from ebisc.celllines import exporter


DOCS = '''
Usage:
  export ecacc
'''


class Command(DocOptCommand):

    docs = DOCS
    help = 'EBISC data exporter'

    def handle_docopt(self, args):

        if args.get('ecacc'):
            exporter.ecacc.run()
