"""Module for app_users application routing."""

from django.contrib.auth.decorators import login_required
from django.urls import path

from app_users.views import (
    SellerProfileView, AuthView, LogoutUserView, OrderDateFilterView, UserProfileView, order_view,
)

urlpatterns = [
    path('profile', UserProfileView.as_view(), name='profile'),
    path('orders', OrderDateFilterView.as_view(), name='orders'),
    path('orders/<int:pk>', order_view, name='order'),
    path('seller', login_required(SellerProfileView.as_view()), name='seller'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', login_required(LogoutUserView.as_view()), name='logout'),
]
