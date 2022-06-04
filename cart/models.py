from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    order_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')

    def __str__(self):
        return f'id:{self.id}\norder_time:{self.order_time}\nuser:{self.user}\nproducts:{self.products.all()}'


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order:{self.order}\nproducts{self.products}\nquantity:{self.quantity}'