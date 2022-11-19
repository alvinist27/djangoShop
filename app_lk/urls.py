from django.urls import path

from app_lk.views import create_product_view, get_products_view, update_product_view, delete_product_view

urlpatterns = [
    path('', get_products_view, name='lk_read'),
    path('add_product', create_product_view, name='lk_create'),
    path('delete_product/<int:id>', delete_product_view, name='lk_delete'),
    path('update_product/<int:id>', update_product_view, name='lk_update'),
]
