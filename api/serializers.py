"""Module with API serializers."""

from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from app_shop.models import Address, Comment, Order, Photo, Product, ProductOrder, RightAccess, SellerData

User = get_user_model()


class AddressSerializer(ModelSerializer):
    """Serializer class for Address model."""

    class Meta:
        """Class with meta information of AddressSerializer."""

        model = Address
        fields = ('id', 'index', 'city', 'street', 'house_number', 'apartment_number')


class RightAccessSerializer(ModelSerializer):
    """Serializer class for RightAccess model."""

    class Meta:
        """Class with meta information of RightAccessSerializer."""

        model = RightAccess
        fields = ('id', 'name')


class UserSerializer(ModelSerializer):
    """Serializer class for User model."""

    access = RightAccessSerializer()

    class Meta:
        """Class with meta information of UserSerializer."""

        model = User
        fields = ('id', 'name', 'surname', 'birth_date', 'email', 'access')


class OrderSerializer(HyperlinkedModelSerializer):
    """Serializer class for Order model."""

    class Meta:
        """Class with meta information of OrderSerializer."""

        model = Order
        fields = ('id', 'created', 'status', 'buyer', 'address')


class PhotoSerializer(HyperlinkedModelSerializer):
    """Serializer class for Photo model."""

    class Meta:
        """Class with meta information of PhotoSerializer."""

        model = Photo
        fields = ('id', 'product', 'file_path')


class SellerDataSerializer(ModelSerializer):
    """Serializer class for SellerData model."""

    legal_address = AddressSerializer()

    class Meta:
        """Class with meta information of SellerDataSerializer."""

        model = SellerData
        fields = ('id', 'user', 'type', 'INN', 'reg_date', 'email', 'legal_name', 'legal_address')


class ProductSerializer(HyperlinkedModelSerializer):
    """Serializer class for Product model."""

    class Meta:
        """Class with meta information of ProductSerializer."""

        model = Product
        fields = (
            'id',
            'name',
            'description',
            'type',
            'category',
            'purchase_price',
            'size',
            'selling_price',
            'quantity',
            'seller',
        )


class CommentSerializer(HyperlinkedModelSerializer):
    """Serializer class for Comment model."""

    class Meta:
        """Class with meta information of CommentSerializer."""

        model = Comment
        fields = ('id', 'product', 'text', 'user_rating', 'created', 'user')


class ProductOrderSerializer(HyperlinkedModelSerializer):
    """Serializer class for ProductOrder model."""

    class Meta:
        """Class with meta information of ProductOrderSerializer."""

        model = ProductOrder
        fields = ('id', 'order', 'price', 'quantity', 'product')
