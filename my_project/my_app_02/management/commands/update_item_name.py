from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Update item name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')
        parser.add_argument('item_name', type=str, help='Item name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('item_name')
        item = Item.objects.filter(pk=pk).first()
        item.item_name = name
        item.save()
        self.stdout.write(f'Название товара {item} изменено')
