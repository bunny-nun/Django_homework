from django.core.management.base import BaseCommand
from my_app_02.models import Customer


class Command(BaseCommand):
    help = 'Create customer'

    def handle(self, *args, **kwargs):
        customer = Customer(
            customer_name='Semen Sidorov',
            email='example3@mail.ru',
            phone_number='+7(915)123-12-32',
            address='address_3',
        )
        customer.save()
        self.stdout.write(
            f'Пользователь {customer.customer_name} добавлен')
