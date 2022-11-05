from django.urls import path

from app_shop.views import MainView, clothes_men_view, clothes_women_view, clothes_child_view, clothes_view


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('clothes/men', clothes_men_view, name='men'),
    path('clothes/women', clothes_women_view, name='women'),
    path('clothes/child', clothes_child_view, name='child'),
    path('clothes/<int:id>', clothes_view, name='clothes'),
]
