from django.http import HttpResponse

from .models import *


def get_customers(request):
    customers = Customer.objects.all()
    return HttpResponse(f'customers: {customers}')


def get_items(request):
    items = Item.objects.all()
    return HttpResponse(f'items: {items}')


def get_orders(request):
    orders = Order.objects.all()
    return HttpResponse(f'orders: {orders}')


