from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app_shop.cart import Cart
from app_shop.forms import ProductCategoryForm, CartAddProductForm, OrderForm
from app_shop.models import Product, ProductOrder


def main_view(request):
    return render(request, 'app_shop/index.html')


def get_products_list(form_select, product_type):
    if form_select != 'Все товары':
        return Product.objects.filter(Q(type=product_type) & Q(category=form_select))[::-1]
    return Product.objects.filter(type=product_type)[::-1]


def product_list_base_view(request, product_type):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        products = None
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
    form = CartAddProductForm()
    return render(request, 'app_shop/product.html', {'item': product, 'form': form})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'app_shop/cart/detail.html', {'cart': cart})


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product, quantity=form.cleaned_data['quantity'], update_quantity=form.cleaned_data['update'])
    else:
        cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart_detail')


def order_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for cloth in cart:
                ProductOrder.objects.create(order=order, cloth=cloth['clothes'],
                    price=cloth['total_price'], quantity=cloth['quantity'])
            cart.clear()
            return render(request, 'app_shop/cart/created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'app_shop/cart/create.html', {'cart': cart, 'form': form})


def order_create(request, id):
    return redirect('/')
