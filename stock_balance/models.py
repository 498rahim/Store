from django.db import models
from stock.models import Stock


class Balance(models.Model):
    name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    count = models.IntegerField()
