from django.core.management.base import BaseCommand
from my_app_02.models import Customer


class Command(BaseCommand):
    help = 'Get all customers'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        self.stdout.write('Список всех пользователей:')
        for customer in customers:
            self.stdout.write(f'{customer}')
