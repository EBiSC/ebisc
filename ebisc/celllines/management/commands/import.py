from django.core.management.base import BaseCommand, CommandError

from ...importer.hotstart import import_hotstart


class Command(BaseCommand):

    args = '<directory>'
    help = 'Import hot start cell line data.'

    def handle(self, *args, **options):
        import_hotstart(args[0])
