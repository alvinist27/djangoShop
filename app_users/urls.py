from django.urls import path

from app_users.views import AuthView, AddSellerView, RegistrationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('seller', AddSellerView.as_view(), name='seller'),
    path('login', AuthView.as_view(), name='login'),
]
