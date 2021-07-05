from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from stock.serializer import Stock, StockSerializer


class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [AllowAny]
    filter_fields = ['name']
