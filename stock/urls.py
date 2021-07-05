from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import StockView

router = DefaultRouter()
router.register('', StockView, '')

urlpatterns = [
    path('', include(router.urls)),
]