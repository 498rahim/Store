from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from order.serializer import OrderProductSerializer, OrderSerializer, OrderProductList
from order.models import OrderProduct, Order
from rest_framework.views import APIView
from django.db.models import Sum, F
from rest_framework.response import Response
from product.models import Product
from rest_framework.generics import ListAPIView


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class OrderProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = OrderProduct.objects.all().values('id',
                                                     'quantity', 'order'
                                                     ).annotate(
            total_price=F('product__price') * F('quantity')
        )
        return Response(queryset)

    def post(self, request):
        serializer = OrderProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderProduct.objects.create(product=serializer.validated_data['product'],
                                    quantity=serializer.validated_data['quantity'],
                                    order=serializer.validated_data['order'])
        return Response({'status': 'done'})


class OrderProductListView(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductList
    permission_classes = [AllowAny]
