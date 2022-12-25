"""Module for app_users views."""

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LogoutView
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from app_shop.forms import DateFilterForm
from app_shop.models import SellerData, Address, RightAccess, Order, ProductOrder
from app_users.forms import ProfileForm, AuthForm, AddSellerForm

User = get_user_model()


class AuthView(FormView):
    """FormView class for user authentication."""

    form_class = AuthForm
    success_url = '/'
    template_name = 'app_users/login.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Send a POST request for AuthView.

        Args:
            request: current request object;
            args: arguments for overriding;
            kwargs: keyword arguments for overriding.

        Returns:
            Response object.
        """
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return self.get(request, *args, **kwargs)


class LogoutUserView(LogoutView):
    """LogoutView class for user logout."""

    next_page = '/'


class UserProfileView(View):
    """View class for user profile."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Send a GET request for ProfileView.

        Args:
            request: current request object.

        Returns:
            Response object.
        """
        user = User.objects.filter(id=request.user.id).first()
        form = ProfileForm(instance=user) if user else ProfileForm()
        return render(request, 'app_users/profile.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        """Send a POST request for ProfileView.

        Args:
            request: current request object.

        Returns:
            Response object.
        """
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if form.cleaned_data['group'] == 'Покупатель':
                return redirect('/')
            return redirect(reverse('seller'))
        return render(request, 'app_users/profile.html', {'form': form})


class SellerProfileView(View):
    """View class for seller's profile."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Send a GET request for AddSellerView.

        Args:
            request: current request object.

        Returns:
            Response object.
        """
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

    def post(self, request: HttpRequest) -> HttpResponse:
        """Send a POST request for AddSellerView.

        Args:
            request: current request object.

        Returns:
            Response object.
        """
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


class OrderDateFilterView(FormView):
    """FormView class for getting user's orders by date filters."""

    form_class = DateFilterForm
    template_name = 'app_users/orders.html'

    def get_success_url(self) -> str:
        """Get success url of sending form to the same view.

        Returns:
            url path to follow after submitting the form.
        """
        return self.request.path

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Send a POST request for OrderDateFilterView.

        Args:
            request: current request object;
            args: arguments for overriding;
            kwargs: keyword arguments for overriding.

        Returns:
            Response object.
        """
        orders = None
        form = DateFilterForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            orders = Order.objects.filter(Q(created__range=(start_date, end_date)) & Q(buyer_id=request.user.id))
        return render(request, self.template_name, {'form': form, 'orders': orders})


def order_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Get user's order by specified id.

    Args:
        request: HttpRequest object;
        pk: id of order to be displayed.

    Returns:
        HttpResponse object.
    """
    order = Order.objects.get(id=pk)
    if order.buyer_id != request.user.id:
        return render(request, 'app_users/error.html')
    products = ProductOrder.objects.filter(order_id=pk)
    return render(request, 'app_users/order.html', {'order': order, 'products': products})
