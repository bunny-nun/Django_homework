from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Update item name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')
        parser.add_argument('quantity', type=int, help='Item quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        quantity = kwargs['quantity']
        item = Item.objects.filter(pk=pk).first()
        item.item_quantity = quantity
        item.save()
        self.stdout.write(f'Количество товара {item} изменено на {quantity} ')
