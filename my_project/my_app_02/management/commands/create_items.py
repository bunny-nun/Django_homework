from django.core.management.base import BaseCommand
from my_app_02.models import Item


class Command(BaseCommand):
    help = 'Generate many items'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Items quantity')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            item = Item(
                item_name=f'Item {i}',
                item_description=f'Lorem ipsum dolor sit amet, consectetur '
                                 f'adipisicing elit. Dolores provident culpa '
                                 f'ea, accusantium quia reprehenderit '
                                 f'assumenda illum nihil suscipit. Neque, fuga'
                                 f' eos! Quae tempore blanditiis, laudantium '
                                 f'iusto molestias accusantium eleniti at, '
                                 f'nihil laboriosam earum illo. Doloribus '
                                 f'cupiditate reiciendis, aut repudiandae '
                                 f'deleniti, voluptatum doloremque expedita '
                                 f'praesentium quibusdam perferendis maiores '
                                 f'explicabo laborum!',
                item_price=i * 100.25,
                item_quantity=i + 50,
            )
            item.save()
        self.stdout.write(
            f'Добавлено {count} товара (-ов)')
