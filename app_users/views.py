"""Module for app_users views."""

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from app_shop.forms import DateFilterForm
from app_shop.models import SellerData, Address, RightAccess, User, Order, ProductOrder
from app_users.forms import ProfileForm, AuthForm, AddSellerForm


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


@method_decorator(login_required, name='dispatch')
class LogoutUserView(LogoutView):
    next_page = '/'


class ProfileView(View):
    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        form = ProfileForm(instance=user) if user else ProfileForm()
        return render(request, 'app_users/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if form.cleaned_data['group'] == 'Покупатель':
                return redirect('/')
            return redirect(reverse('seller'))
        return render(request, 'app_users/profile.html', {'form': form})


class AddSellerView(View):
    def get(self, request):
        seller = SellerData.objects.filter(user_id=request.user.id).first()
        if seller:
            form = AddSellerForm(
                initial={
                    'index': seller.legal_address.index,
                    'city': seller.legal_address.city,
                    'street': seller.legal_address.street,
                    'house_number': seller.legal_address.house_number,
                },
                instance=seller,
            )
        else:
            form = AddSellerForm()
        return render(request, 'app_users/seller.html', {'form': form})

    def post(self, request):
        form = AddSellerForm(request.POST)
        if form.is_valid():
            address = Address.objects.create(
                index=form.cleaned_data['index'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                house_number=form.cleaned_data['house_number'],
            )

            SellerData.objects.update_or_create(
                user=request.user,
                defaults={
                    'type': form.cleaned_data['type'],
                    'INN': form.cleaned_data['INN'],
                    'reg_date': form.cleaned_data['reg_date'],
                    'email': form.cleaned_data['email'],
                    'legal_name': form.cleaned_data['legal_name'],
                    'legal_address': address,
                },
            )

            access = RightAccess.objects.get(name='Продавец')
            request.user.access = access
            request.user.save()

        return render(request, 'app_users/seller.html', {'form': form})


class OrderListView(View):
    def get(self, request):
        form = DateFilterForm()
        return render(request, 'app_users/orders.html', {'form': form})

    def post(self, request):
        orders = None
        form = DateFilterForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            orders = Order.objects.filter(Q(created__range=(start_date, end_date)) & Q(buyer_id=request.user.id))
        return render(request, 'app_users/orders.html', {'form': form, 'orders': orders})


class OrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        if order.buyer_id != request.user.id:
            return render(request, 'app_users/error.html')
        products = ProductOrder.objects.filter(order_id=pk)
        return render(request, 'app_users/order.html', {'order': order, 'products': products})
