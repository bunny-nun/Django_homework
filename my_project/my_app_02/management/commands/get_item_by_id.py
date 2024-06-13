from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Get item by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        item = Item.objects.filter(pk=pk).first()
        self.stdout.write(f'Найден товар с id {pk}: {item}')


