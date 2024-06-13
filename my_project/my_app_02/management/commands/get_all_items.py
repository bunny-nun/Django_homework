from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Get all items'

    def handle(self, *args, **kwargs):
        items = Item.objects.all()
        self.stdout.write('Список всех товаров:')
        for item in items:
            self.stdout.write(f'{item}')
