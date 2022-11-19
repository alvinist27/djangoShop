from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from app_shop.forms import ProductCategoryForm
from app_shop.models import Product


class MainView(View):
    def get(self, request):
        return render(request, 'app_shop/index.html')


def get_products_list(form_select, product_type):
    if form_select != 'Все товары':
        return Product.objects.filter(Q(type=product_type) & Q(category=form_select))[::-1]
    return Product.objects.filter(type=product_type)[::-1]


def product_list_base_view(request, product_type):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            products = get_products_list(select, product_type)
    else:
        form = ProductCategoryForm()
        products = get_products_list('Все товары', product_type)
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'app_shop/products_list.html', {'name': f'{product_type} одежда', 'clothes': page_obj, 'form': form},
    )


def men_products_list_view(request):
    return product_list_base_view(request, 'Мужская')


def women_products_list_view(request):
    return product_list_base_view(request, 'Женская')


def child_products_list_view(request):
    return product_list_base_view(request, 'Детская')


def product_view(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'app_shop/product.html', {'item': product})
