from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from ...importer import hotstart
from ...models import *


class Command(BaseCommand):

    args = '<directory>'
    help = 'Import hot start cell line data'

    option_list = BaseCommand.option_list + (
        make_option('--init',
            action='store_true',
            dest='init',
            default=False,
            help='Delete existing records before the import'),)

    def handle(self, *args, **options):

        if options['init']:
            for model in [Disease, Celltype, Celllineorgtype, Organization, Cellline]:
                model.objects.all().delete()

        hotstart.import_data(args[0])
