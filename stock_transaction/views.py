from rest_framework.views import APIView
from stock_transaction.serializer import TransactionSerializer
from rest_framework.response import Response
from stock_transaction.models import StockTransaction
from rest_framework.permissions import AllowAny


class TransactionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = StockTransaction.objects.all().values('id', 'stock__name', 'product__name', 'product__price',
                                                         'quantity', )

        return Response(queryset)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        StockTransaction.objects.create(product=serializer.validated_data['product'],
                                        stock=serializer.validated_data['stock'],
                                        quantity=serializer.validated_data['quantity'],
                                        )
        return Response({'status': 'done'})
