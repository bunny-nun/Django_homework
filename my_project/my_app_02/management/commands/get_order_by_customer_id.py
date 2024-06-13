from django.core.management.base import BaseCommand
from my_app_02.models import Customer, Order


class Command(BaseCommand):
    help = 'Get all orders by customer id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            orders = Order.objects.filter(customer=customer)
            self.stdout.write(f'All orders of {customer.customer_name}:')
            for order in orders:
                self.stdout.write(f'id {order.id}\n')
