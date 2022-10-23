from django.urls import path
from app_users.views import AuthView, RegistrationView, LogoutUserView, UpdateUserView


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', AuthView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('profile', UpdateUserView.as_view(), name='profile'),
]
