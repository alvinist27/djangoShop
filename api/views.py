"""Module for api views."""

# https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/readme
# https://blog.logrocket.com/django-rest-framework-create-api/
# https://www.django-rest-framework.org/tutorial/quickstart/

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers import AddressSerializer
from app_shop.models import Address, Comment, Order, Product, ProductOrder, SellerData


class AddressViewSet(ModelViewSet):
    """API endpoint that allows Address objects to be viewed or edited."""

    queryset = Address.objects.all().order_by('-id')
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
