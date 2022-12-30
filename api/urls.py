"""Module for api routing."""

from django.urls import include, path
from rest_framework import routers

from api.views import (
    AddressViewSet, CommentViewSet, OrderViewSet, PhotoViewSet, ProductViewSet, ProductOrderViewSet, RightAccessViewSet,
    SellerDataViewSet, UserViewSet,
)

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'order', OrderViewSet)
router.register(r'photo', PhotoViewSet)
router.register(r'product', ProductViewSet)
router.register(r'product_order', ProductOrderViewSet)
router.register(r'right_access', RightAccessViewSet)
router.register(r'seller_data', SellerDataViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
