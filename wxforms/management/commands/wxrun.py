from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<app_name *args>'
    help = 'run main.py in the selected app'
    def handle(self, *args, **options):
        if len(args)<1:
            raise CommandError("Need at least one argument")
        try:
            main = __import__(args[0]+".main",fromlist=['main'])
        except ImportError as error:
            raise CommandError(args[0]+".main not found")
        args = args[1:]
        try:
            main.main(*args,**options)
        except TypeError as error:
            raise CommandError(error.message)
