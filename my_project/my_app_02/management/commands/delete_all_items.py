from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Delete all items'

    def handle(self, *args, **kwargs):
        items = Item.objects.all()
        for item in items:
            if item is not None:
                item.delete()
        self.stdout.write(f'Все товары удалены')
