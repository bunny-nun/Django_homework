import logging
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, ItemForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'my_app_02/index.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            logger.info(
                f'Получены данные пользователя {customer_name=}, {email=}, '
                f'{phone_number=}, {address=}')
            hashed_password = make_password(password)
            customer = Customer(customer_name=customer_name, email=email,
                                phone_number=phone_number, address=address,
                                password=hashed_password)
            customer.save()
            message = 'Пользователь успешно сохранен'
            return redirect('registration_success')
        else:
            message = 'Ошибка в данных'
    else:
        form = CustomerForm()
        message = 'Заполните форму'
    context = {
        'title': 'Регистрация',
        'form': form,
        'message': message,
    }
    return render(request, 'my_app_02/register.html', context)


def registration_success(request):
    context = {'title': 'Успешная регистрация'}
    return render(request,
                  'my_app_02/registration_success.html', context)


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
    context = {'title': 'Заказы',
               'customer': customer,
               'items_7_days': order_items_7_days,
               'items_30_days': order_items_30_days,
               'items_365_days': order_items_365_days}
    return render(request, 'my_app_02/orders.html', context)


def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_description = form.cleaned_data['item_description']
            item_price = form.cleaned_data['item_price']
            item_quantity = form.cleaned_data['item_quantity']
            item_image = form.cleaned_data['item_image']
            fs = FileSystemStorage()
            image_path = fs.save(item_image.name, item_image)
            item = Item(item_name=item_name, item_description=item_description,
                        item_price=item_price, item_quantity=item_quantity,
                        item_image=image_path)
            item.save()
            form = ItemForm()
    else:
        form = ItemForm()
    context = {
        'title': 'Новый товар',
        'form': form,
    }
    return render(request, 'my_app_02/new_item.html', context)


def page_not_found(request, exception):
    context = {'title': 'Страница не найдена'}
    return render(request, "my_app_02/404.html", context, status=404)
