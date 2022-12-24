"""Module for app_lk application routing."""

from django.contrib.auth.decorators import login_required
from django.urls import path

from app_lk.views import create_product_view, get_products_view, update_product_view, delete_product_view

urlpatterns = [
    path('', login_required(get_products_view), name='lk_read'),
    path('add_product', login_required(create_product_view), name='lk_create'),
    path('delete_product/<int:id>', login_required(delete_product_view), name='lk_delete'),
    path('update_product/<int:id>', login_required(update_product_view), name='lk_update'),
]
