"""Admin module of app_users application."""

from typing import List

from django.contrib.admin import AdminSite
from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import FormView

from app_shop.forms import DateFilterForm
from app_shop.models import Product, Order, ProductOrder
from app_users.tasks import send_mail_notification


class StatisticsAdminView(FormView):
    """FormView class for getting products statistics by date filters."""

    admin_site = None
    form_class = DateFilterForm
    template_name = 'app_users/admin/statistics.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Send a POST request for StatisticsAdminView.

        Args:
            request: current request object;
            args: arguments for overriding;
            kwargs: keyword arguments for overriding.

        Returns:
            Response object.
        """
        form = DateFilterForm(request.POST)
        products = None
        profit_products = None

        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            products = ProductOrder.objects.filter(
                order__created__range=(start_date, end_date),
            ).select_related('product').order_by('-quantity')[:5]

            profit_products = ProductOrder.objects.filter(order__created__range=(start_date, end_date)).annotate(
                result=F('quantity') * (F('product__selling_price') - F('product__purchase_price')),
            ).order_by('-result')[:5]

        return render(request, self.template_name, {
            'form': form, 'products': products, 'profit_products': profit_products,
        })


def send_mail_to_all(request) -> HttpResponse:
    """Send Email notification to registered users.

    Args:
        request: current request object.

    Returns:
        Response object.
    """
    send_mail_notification.delay()
    return HttpResponse('Уведомления отправлены на адреса электронной почты покупателей')


class CustomAdminSite(AdminSite):
    """Custom AdminSite class."""

    site_header = 'Страница администратора'
    site_title = 'Страница администратора магазина'

    def get_urls(self) -> List:
        """Get URLs of additional defined views.

        Returns:
            URLs to be used in custom admin panel.
        """
        urls = super().get_urls()
        my_urls = [
            path('products/', self.admin_view((StatisticsAdminView.as_view(admin_site=self))), name='products'),
            path('send_notifications/', self.admin_view(send_mail_to_all), name='products'),
        ]

        return my_urls + urls


admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Order)
admin_site.register(Product)
