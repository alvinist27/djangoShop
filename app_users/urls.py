from django.contrib.auth.decorators import login_required
from django.urls import path

from app_users.views import AddSellerView, AuthView, LogoutUserView, ProfileView

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('seller', login_required(AddSellerView.as_view()), name='seller'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
]
