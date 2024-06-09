from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=128, unique=True)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class Item(models.Model):
    item_name = models.CharField(max_length=128)
    item_description = models.TextField(default=None)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_quantity = models.PositiveIntegerField()
    item_addition_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.item_name} ({self.item_price} рублей)'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def update_total_amount(self):
        self.order.total_amount += self.item.item_price * self.quantity
        self.order.save()
