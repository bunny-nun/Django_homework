from django.urls import path
from . import views

handler404 = views.page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:customer_id>/', views.customer_orders_7_days,
         name='orders'),
    path('register/', views.register, name='registration'),
    path('registration_success/', views.registration_success,
         name='registration_success'),
    path('new_item/', views.new_item, name='new_item'),
]