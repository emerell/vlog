from django.core.management.base import BaseCommand
from vlog import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Tag.objects.all().delete()

        self.stdout.write('Successfully deleted all the tags')