from django.urls import path
from stock_transaction.views import TransactionView

urlpatterns = [
    path('', TransactionView.as_view()),
]
