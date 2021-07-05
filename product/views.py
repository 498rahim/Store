from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from product.serializer import Product, ProductSerializer


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
