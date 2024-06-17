from django.core.management.base import BaseCommand
import random
from my_app_03.models import Customer


class Command(BaseCommand):
    help = 'Create customer'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Customers quantity')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            number = str(i).zfill(7)

            customer = Customer(
                customer_name=f'Customer {i}',
                email=f'example{i}@mail.ru',
                phone_number=f'+7915{number}',
                address=f'address {i}',
            )
            customer.save()
            self.stdout.write(
                f'Пользователь {customer.customer_name} добавлен')
