from django.urls import path
from stock_balance.views import BalanceView

urlpatterns = [
    path('', BalanceView.as_view()),
]
