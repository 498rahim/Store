from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderProductView, OrderProductListView, OrderView

router = DefaultRouter()
router.register('info', OrderView, 'info/')
router.register('list', OrderProductListView, 'list/')

urlpatterns = [
    path('', OrderProductView.as_view()),
    path('', include(router.urls)),
]
