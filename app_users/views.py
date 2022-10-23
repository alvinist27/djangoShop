from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from app_users.forms import RegistrationForm, AuthForm, UpdateUserForm
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'app_users/register.html', {'form': form})


class AuthView(LoginView):
    template_name = 'app_users/login.html'
    form_class = AuthForm


@method_decorator(login_required, name='dispatch')
class LogoutUserView(LogoutView):
    next_page = '/'


@method_decorator(login_required, name='dispatch')
class UpdateUserView(View):
    def get(self, request):
        form = UpdateUserForm(instance=request.user)
        return render(request, 'app_users/profile.html', {'form': form})

    def post(self, request):
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(request, 'app_users/profile.html', {'form': form})