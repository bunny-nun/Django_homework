from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def header_menu():
    menu = [{'title': "Главная", 'url': '/'},
            {'title': "Блузки и рубашки", 'url': '/top/'},
            {'title': "Брюки", 'url': '/pants/'},
            {'title': "Обувь", 'url': '/shoes/'},
            {'title': "Контакты", 'url': '/contacts/'}]
    return menu


def index(request):

    context = {'menu': header_menu(),
               'title': 'Главная',
               'cur_url': '/'}
    return render(request, 'my_app_02/index.html', context)
