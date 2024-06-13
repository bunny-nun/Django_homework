from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Generate many items'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Item quantity')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            item = Item(
                item_name=f'Item {i}',
                item_description=f'Description {i}',
                item_price=f'{i * 100.01}',
                item_quantity=f'{i + 5}', )
            item.save()
        self.stdout.write(
            f'Добавлено {count} товара (-ов)')
