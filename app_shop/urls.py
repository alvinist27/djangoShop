from django.urls import path

from app_shop.views import (
    main_view, men_products_list_view, women_products_list_view, child_products_list_view, product_view, cart_detail,
    cart_add, cart_remove, order_cart, order_create, about_view,
)

urlpatterns = [
    path('', main_view, name='main'),
    path('about/', about_view, name='about'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('cart_add/<int:id>', cart_add, name='cart_add'),
    path('cart_remove/<int:id>', cart_remove, name='cart_remove'),
    path('order_cart/', order_cart, name='order_cart'),
    path('order_create/<int:id>', order_create, name='order_create'),
    path('products/men', men_products_list_view, name='men'),
    path('products/women', women_products_list_view, name='women'),
    path('products/child', child_products_list_view, name='child'),
    path('product/<int:id>', product_view, name='product'),
]
