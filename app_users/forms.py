from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from app_shop.models import User


class AuthForm(AuthenticationForm):
    username = forms.CharField(max_length=80, required=True, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=40, required=True, label='Имя пользователя')
    surname = forms.CharField(max_length=50, required=True, label='Имя пользователя')
    email = forms.EmailField(label='Email адрес', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Повторите пароль')

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=80, required=True, label='Имя пользователя')
    email = forms.EmailField(label='Email адрес')
    first_name = forms.CharField(max_length=150, label='Имя')
    last_name = forms.CharField(max_length=150, label='Фамилия')

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password')
