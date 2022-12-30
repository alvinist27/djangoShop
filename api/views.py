"""Module for api views."""

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.serializers import (
    CommentSerializer, OrderSerializer, PhotoSerializer, ProductSerializer, ProductOrderSerializer,
    RightAccessSerializer, SellerDataSerializer, UserSerializer, AddressSerializer,
)
from app_shop.models import Address, Comment, Order, Photo, Product, ProductOrder, RightAccess, SellerData

User = get_user_model()


class AddressViewSet(ModelViewSet):
    """API endpoint that allows Address objects to be viewed or edited."""

    queryset = Address.objects.all().order_by('-id')
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(ModelViewSet):
    """API endpoint that allows Comment objects to be viewed or edited."""

    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    """API endpoint that allows Order objects to be viewed or edited."""

    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class PhotoViewSet(ModelViewSet):
    """API endpoint that allows Photo objects to be viewed or edited."""

    queryset = Photo.objects.all().order_by('-id')
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    """API endpoint that allows Product objects to be viewed or edited."""

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductOrderViewSet(ModelViewSet):
    """API endpoint that allows ProductOrder objects to be viewed or edited."""

    queryset = ProductOrder.objects.all().order_by('-id')
    serializer_class = ProductOrderSerializer
    permission_classes = [IsAuthenticated]


class RightAccessViewSet(ReadOnlyModelViewSet):
    """API endpoint that allows RightAccess objects to be viewed."""

    queryset = RightAccess.objects.all()
    serializer_class = RightAccessSerializer
    permission_classes = [IsAuthenticated]


class SellerDataViewSet(ModelViewSet):
    """API endpoint that allows SellerData objects to be viewed or edited."""

    queryset = SellerData.objects.all().order_by('-id')
    serializer_class = SellerDataSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    """API endpoint that allows User objects to be viewed or edited."""

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
