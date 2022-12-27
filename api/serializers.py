"""Module with API serializers."""

from rest_framework.serializers import HyperlinkedModelSerializer
from app_shop.models import Address, Comment, Order, Product, ProductOrder, SellerData

from django.contrib.auth import get_user_model


User = get_user_model()


class AddressSerializer(HyperlinkedModelSerializer):
    """Serializer class for Address model."""

    class Meta:
        """Class with meta information of AddressSerializer."""

        model = Address
        fields = ('id', 'index', 'city', 'street', 'house_number', 'apartment_number')
