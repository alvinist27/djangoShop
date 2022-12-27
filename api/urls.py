"""Module for api routing."""

from django.urls import include, path
from rest_framework import routers

from api.views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
