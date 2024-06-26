from django.core.management.base import BaseCommand
from my_app_02.models import *


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Item quantity')

    def handle(self, *args, **kwargs):
        customer = 5
        try:
            customer = Customer.objects.get(pk=customer)
        except Customer.DoesNotExist:
            self.stdout.write(self.style.ERROR('Customer not found'))
            return

        total_amount = 0
        order = Order(
            customer=customer,
            total_amount=total_amount
        )
        order.save()

        items = Item.objects.all()
        count = kwargs.get('count')

        for i in range(0, 15, 8):
            item = items[i]
            quantity = count if item.item_quantity >= count else item.item_quantity
            order_item = OrderItem(
                order=order,
                item=item,
                quantity=quantity,
            )
            order_item.save()
            order_item.update_amount()
        order.save()

        self.stdout.write(
            f'Заказ id {order.id} добавлен')
