from django.db import models
from product.models import Product
from stock.models import Stock


class StockTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    date_at = models.DateTimeField(auto_now_add=True)
