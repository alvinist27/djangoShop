from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from app_users.forms import RegistrationForm, AuthForm
from django.views import View


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, 'app_users/register.html', {'form': form})


class AuthView(View):
    def get(self, request):
        form = AuthForm()
        return render(request, 'app_users/login.html', {'form': form})

    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'app_users/login.html', {'form': form})
