"""Admin module of app_users application."""

from django.contrib.admin import AdminSite
from django.db.models import F
from django.shortcuts import render
from django.urls import path
from django.views import View

from app_shop.forms import DateFilterForm
from app_shop.models import Product, Order, ProductOrder


class StatisticsAdminView(View):
    admin_site = None

    def get(self, request):
        form = DateFilterForm()
        return render(request, 'app_users/admin/statistics.html', {'form': form})

    def post(self, request):
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

        return render(request, 'app_users/admin/statistics.html', {
            'form': form, 'products': products, 'profit_products': profit_products,
        })


class CustomAdminSite(AdminSite):
    site_header = 'Страница администратора магазина'
    site_title = 'Страница администратора магазина'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('products/', self.admin_view((StatisticsAdminView.as_view(admin_site=self))), name='products'),
        ]

        return my_urls + urls


admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Order)
admin_site.register(Product)
