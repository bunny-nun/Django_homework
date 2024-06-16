from django.core.management.base import BaseCommand
from my_app_02.models import Customer


class Command(BaseCommand):
    help = 'Update customer name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('customer_name', type=str, help='Customer name')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['customer_name']
        customer = Customer.objects.filter(pk=pk).first()
        customer.customer_name = name
        customer.save()
        self.stdout.write(f'Имя пользователя {customer} изменено')
