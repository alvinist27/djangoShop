from django.urls import path

from app_users.views import AuthView, RegistrationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', AuthView.as_view(), name='login'),
]
