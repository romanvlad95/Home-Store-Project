from django.db import models
from goods.models import Products
from users.models import User


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="User",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Order Creation Date")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    requires_delivery = models.BooleanField(default=False, verbose_name="Requires Delivery")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Delivery Address")
    payment_on_get = models.BooleanField(default=False, verbose_name="Payment on Delivery")
    is_paid = models.BooleanField(default=False, verbose_name="Paid")
    status = models.CharField(max_length=50, default='Processing', verbose_name="Order Status")

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ('id',)

    def __str__(self):
        return f"Order № {self.pk} | Customer {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Order")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Product",
                                default=None)
    name = models.CharField(max_length=150, verbose_name="Name")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Sale Date")

    class Meta:
        db_table = "order_item"
        verbose_name = "Sold Item"
        verbose_name_plural = "Sold Items"
        ordering = ('id',)

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.name} | Order № {self.order.pk}"
