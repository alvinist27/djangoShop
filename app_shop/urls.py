"""Module for app_shop application routing."""

from django.urls import path

from app_shop.views import (
    main_view, men_products_list_view, women_products_list_view, child_products_list_view, product_view, cart_detail,
    cart_add, cart_remove, order_cart, order_product, about_view, search_products,
)

urlpatterns = [
    path('', main_view, name='main'),
    path('about/', about_view, name='about'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('cart_add/<int:id>', cart_add, name='cart_add'),
    path('cart_remove/<int:id>', cart_remove, name='cart_remove'),
    path('order_cart/', order_cart, name='order_cart'),
    path('order_product/<int:id>', order_product, name='order_product'),
    path('products/men', men_products_list_view, name='men'),
    path('products/women', women_products_list_view, name='women'),
    path('products/child', child_products_list_view, name='child'),
    path('product/<int:id>', product_view, name='product'),
    path('search/', search_products, name='search_products'),
]
