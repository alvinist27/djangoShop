from django.urls import path

from app_shop.views import (
    MainView, men_products_list_view, women_products_list_view, child_products_list_view, product_view,
)


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('products/men', men_products_list_view, name='men'),
    path('products/women', women_products_list_view, name='women'),
    path('products/child', child_products_list_view, name='child'),
    path('product/<int:id>', product_view, name='product'),
]
