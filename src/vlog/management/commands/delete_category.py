from django.core.management.base import BaseCommand, CommandError
from vlog.models import Category


class Command(BaseCommand):
    help = 'Delete a category with the specified id(s)'

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=int)

    def handle(self, *args, **options):
        category_id = options['category_id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise CommandError('Category "%s" does not exist' % category_id)

        category.save()
        self.stdout.write('Successfully deleted category with title "%s"' % category.title)
