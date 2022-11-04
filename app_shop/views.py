from app_shop.models import Product
from django.views import View
from django.db.models import Q
from app_shop.forms import ProductCategoryForm
from django.core.paginator import Paginator
from django.shortcuts import render


class MainView(View):
    def get(self, request):
        return render(request, 'app_shop/index.html')


def get_clothes_list(form_select, cloth_type):
    if form_select != 'Все товары':
        return Product.objects.filter(Q(type=cloth_type) & Q(category=form_select))[::-1]
    return Product.objects.filter(type=cloth_type)[::-1]


def clothes_base_view(request, cloth_type):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data.get('select')
            clothes = get_clothes_list(select, cloth_type)
        else:
            clothes = []
    else:
        form = ProductCategoryForm()
        clothes = Product.objects.filter(type=cloth_type)[::-1]
    paginator = Paginator(clothes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/clothes_list.html',
                  {'name': f'{cloth_type} одежда', 'clothes': page_obj, 'form': form})


def clothes_men_view(request):
    return clothes_base_view(request, 'Мужская')


def clothes_women_view(request):
    return clothes_base_view(request, 'Женская')


def clothes_child_view(request):
    return clothes_base_view(request, 'Детская')
