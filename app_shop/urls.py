from django.urls import path
from app_shop import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('clothes/men', views.clothes_men_view, name='men'),
    path('clothes/women', views.clothes_women_view, name='women'),
    path('clothes/child', views.clothes_child_view, name='child'),
    # path('clothes/<int:id>', views.clothes_view, name='clothes'),
    # path('order_create/', views.order_create, name='order_create'),
]