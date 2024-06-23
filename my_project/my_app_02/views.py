from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
from datetime import timedelta


def header_menu():
    menu = [{'title': "Главная", 'url': '/'},
            {'title': "Блузки и рубашки", 'url': 'my_app_02/top/'},
            {'title': "Брюки", 'url': 'my_app_02/pants/'},
            {'title': "Обувь", 'url': 'my_app_02/shoes/'},
            {'title': "Заказы", 'url': 'my_app_02/orders/'}]
    return menu


def index(request):
    cur_url = request.path
    context = {'menu': header_menu(),
               'title': 'Главная',
               'cur_url': cur_url}
    return render(request, 'my_app_02/index.html', context)


def get_customer_orders(customer, days):
    time_now = timezone.now()
    orders = Order.objects.filter(customer=customer,
                                  order_date__gte=time_now - timedelta(
                                      days=days)).order_by('order_date')
    all_order_items = list()
    for order in orders:
        order_items = OrderItem.objects.filter(order=order)
        for i in order_items:
            item = Item.objects.filter(pk=i.item_id).first()
            if item not in all_order_items:
                all_order_items.append(item)
    return all_order_items


def customer_orders_7_days(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    order_items_7_days = get_customer_orders(customer, 7)
    order_items_30_days = get_customer_orders(customer, 30)
    order_items_365_days = get_customer_orders(customer, 365)
    cur_url = request.path
    context = {'menu': header_menu(),
               'title': 'Главная',
               'cur_url': cur_url,
               'customer': customer,
               'items_7_days': order_items_7_days,
               'items_30_days': order_items_30_days,
               'items_365_days': order_items_365_days}
    return render(request, 'my_app_02/orders.html', context)


def page_not_found(request, exception):
    cur_url = request.path
    context = {'menu': header_menu(),
               'title': 'Страница не найдена',
               'cur_url': cur_url}
    return render(request, "my_app_02/404.html", context, status=404)
