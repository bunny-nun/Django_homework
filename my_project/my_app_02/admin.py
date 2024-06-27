from django.contrib import admin
from .models import *


@admin.action(description='Сбросить количество на ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(item_quantity=0)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'email', 'phone_number',
                    'address', 'registration_date']
    fields = ['customer_name', 'email', 'phone_number',
              'address', 'registration_date']
    readonly_fields = ['registration_date']
    ordering = ['customer_name']
    search_fields = ['customer_name']
    search_help_text = ['Поиск по имени клиента']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_description', 'item_price',
                    'item_quantity']
    fields = ['item_name', 'item_description', 'item_price',
              'item_quantity', 'item_addition_date']
    readonly_fields = ['item_addition_date']
    ordering = ['item_price', 'item_name']
    list_filter = ['item_price', 'item_quantity']
    search_fields = ['item_name', 'item_description']
    search_help_text = ['Поиск по наименованию или описанию товара']
    actions = [reset_quantity]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_amount', 'order_date']
    list_filter = ['customer', 'total_amount', 'order_date']
    readonly_fields = ['order_date']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
