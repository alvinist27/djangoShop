from django.contrib.auth.decorators import login_required
from django.urls import path

from app_users.views import AddSellerView, AuthView, LogoutUserView, OrderView, OrderListView, ProfileView

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('orders', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', OrderView.as_view(), name='order'),
    path('seller', login_required(AddSellerView.as_view()), name='seller'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
]
