from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Update item name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')
        parser.add_argument('item_price', type=float, help='Item price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('item_price')
        item = Item.objects.filter(pk=pk).first()
        item.item_price = price
        item.save()
        self.stdout.write(f'Цена товара {item} изменена')
