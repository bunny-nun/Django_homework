from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.get_customers, name='customers'),
    path('items/', views.get_items, name='items'),
    path('orders/', views.get_orders, name='orders'),
]