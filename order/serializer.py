from rest_framework import serializers
from order.models import Order, OrderProduct
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(default=1)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())


class OrderProductList(serializers.ModelSerializer):
    product_info = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'product_info', 'quantity', 'order']

    def get_product_info(self, obj):
        return Product.objects.filter(name=obj.product).values('name', 'price')
