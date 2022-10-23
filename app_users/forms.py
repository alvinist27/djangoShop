from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_shop.models import User


class AuthForm(forms.Form):
    email = forms.CharField(max_length=50, required=True, label='Email адрес')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    captcha = CaptchaField(label='Captcha')


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=40, required=True, label='Имя пользователя')
    surname = forms.CharField(max_length=50, required=True, label='Фамилия пользователя')
    email = forms.EmailField(label='Email адрес', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Повторите пароль')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password1', 'password2')
