from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from stock_transaction.models import StockTransaction
from django.db.models import Sum, F


class BalanceView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        stock = int(request.GET.get('stock_id'))
        product = StockTransaction.objects.values(
            'product__name'
        ).annotate(
            stock=Sum('quantity'), total_sum=F('product__price') * Sum('quantity'))
        return Response({'stock_id': stock, 'result': product})
