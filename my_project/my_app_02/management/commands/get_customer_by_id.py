from django.core.management.base import BaseCommand
from my_app_02.models import Customer


class Command(BaseCommand):
    help = 'Get customer by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        customer = Customer.objects.filter(pk=pk).first()
        self.stdout.write(f'Найден пользователь с id {pk}: {customer}')


