from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    customer_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    address = models.TextField()
    password = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class Item(models.Model):
    item_name = models.CharField(max_length=128)
    item_description = models.TextField(default=None)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_quantity = models.PositiveIntegerField()
    item_image = models.ImageField(default=None)
    item_addition_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.item_name} ({self.item_price} рублей)'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ № {self.pk} ({self.order_date})'


# я ввела дополнительный класс OrderItem, так как покупатель
# не обязательно выкупает все количество товара в наличии, а поле ManyToMany
# в классе Order не позволит включить только часть количества

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def update_amount(self):
        self.order.total_amount += self.item.item_price * self.quantity
        self.order.save()
        self.item.item_quantity -= self.quantity
        self.item.save()
