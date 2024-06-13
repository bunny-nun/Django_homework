from django.core.management.base import BaseCommand
from my_app_02.models import Customer


class Command(BaseCommand):
    help = 'Create customer'

    def handle(self, *args, **kwargs):
        customer = Customer(
            customer_name='Alla Ghukova',
            email='example4@mail.ru',
            phone_number='+79151231231',
            address='address_4',
        )
        customer.save()
        self.stdout.write(
            f'Пользователь {customer.customer_name} добавлен')
