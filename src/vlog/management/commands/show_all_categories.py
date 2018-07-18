from django.core.management.base import BaseCommand
from vlog.models import Category


class Command(BaseCommand):
    args = ''

    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            self.stdout.write('Category ID = "%s"' % category.id)
            self.stdout.write('\nCategory title = "%s"' % category.title)
            self.stdout.write('\nCategory created date = "%s"' % category.created)
            self.stdout.write('\n\n\n')