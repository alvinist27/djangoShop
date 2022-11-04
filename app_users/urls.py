from django.contrib.auth.decorators import login_required
from django.urls import path

from app_users.views import AddSellerView, AuthView, LogoutUserView, RegistrationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('seller', login_required(AddSellerView.as_view()), name='seller'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
]
