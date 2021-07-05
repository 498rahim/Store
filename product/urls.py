from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductAPIView

router = DefaultRouter()
router.register('', ProductAPIView, '')

urlpatterns = [
    path('', include(router.urls)),
]
