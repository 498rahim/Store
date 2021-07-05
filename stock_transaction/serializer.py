from rest_framework import serializers
from stock.models import Stock
from product.models import Product


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    stock = serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all())
    quantity = serializers.IntegerField()
