from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Order(models.Model):
    NEW = 'new'
    PAY = 'pay'
    STATUS = ((PAY, PAY), (NEW, NEW))
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=72, choices=STATUS, default="new")


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)