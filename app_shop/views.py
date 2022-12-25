"""Module for app_shop views."""

from typing import List

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import FormView

from app_shop.cart import Cart
from app_shop.choices import OrderStatusChoices
from app_shop.forms import ProductCategoryForm, CartAddProductForm, OrderForm, CommentForm
from app_shop.models import Product, ProductOrder, Order, Address, Comment

PER_PAGE_RESULTS = 12


def main_view(request: HttpRequest) -> HttpResponse:
    """Display the main page of the shop.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    return render(request, 'app_shop/index.html')


def about_view(request: HttpRequest) -> HttpResponse:
    """Display page with information about shop.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    return render(request, 'app_shop/about.html')


def search_products(request: HttpRequest) -> HttpResponse:
    """Get products by user's search query.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else None
    paginator = Paginator(products, PER_PAGE_RESULTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/search.html', {'products': page_obj, 'count': paginator.count})


def get_products_list(form_select: str, product_type: str) -> List[Product]:
    """Get products by category and type.

    Args:
        form_select: Category of the displayed product list;
        product_type: Type of the displayed product list.

    Returns:
        List of products corresponding to category and type.
    """
    if form_select != 'Все товары':
        return Product.objects.filter(Q(type=product_type) & Q(category=form_select)).order_by('-id')
    return Product.objects.filter(type=product_type).order_by('-id')


def product_list_base_view(request: HttpRequest, product_type: str) -> HttpResponse:
    """Base view for getting products list by type.

    Args:
        request: HttpRequest object.
        product_type: Type of the displayed product list.

    Returns:
        HttpResponse object.
    """
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        products = None
        if form.is_valid():
            select = form.cleaned_data.get('select')
            products = get_products_list(select, product_type)
    else:
        form = ProductCategoryForm()
        products = get_products_list('Все товары', product_type)
    paginator = Paginator(products, PER_PAGE_RESULTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'app_shop/products_list.html', {'name': f'{product_type} одежда', 'products': page_obj, 'form': form},
    )


def men_products_list_view(request: HttpRequest) -> HttpResponse:
    """Get list of men's products.

    Args:
       request: HttpRequest object.

    Returns:
       HttpResponse object.
    """
    return product_list_base_view(request, 'Мужская')


def women_products_list_view(request: HttpRequest) -> HttpResponse:
    """Get list of women's products.

    Args:
       request: HttpRequest object.

    Returns:
       HttpResponse object.
    """
    return product_list_base_view(request, 'Женская')


def child_products_list_view(request: HttpRequest) -> HttpResponse:
    """Get list of child's products.

    Args:
       request: HttpRequest object.

    Returns:
       HttpResponse object.
    """
    return product_list_base_view(request, 'Детская')


def product_view(request: HttpRequest, id: int) -> HttpResponse:
    """Get product by id.

    Args:
       request: HttpRequest object;
       id: selected product id.

    Returns:
       HttpResponse object.
    """
    rating = 'Нет оценок'
    product = Product.objects.filter(id=id).first()
    form = CartAddProductForm()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment = Comment(user=request.user, product=product)
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
    comment_list = Comment.objects.filter(product=id)
    if comment_list:
        rating = round(sum([i[0] for i in list(comment_list.values_list('user_rating'))]) / len(comment_list), 2)
    paginator = Paginator(comment_list, PER_PAGE_RESULTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_shop/product.html', {
        'item': product, 'form': form, 'comment_form': comment_form, 'comment_list': page_obj, 'rating': rating,
    })


def cart_detail(request: HttpRequest) -> HttpResponse:
    """Display user's shopping cart.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    return render(request, 'app_shop/cart/detail.html', {'cart': Cart(request)})


@require_POST
def cart_add(request: HttpRequest, id: int) -> HttpResponse:
    """Add product to user's shopping cart.

    Args:
        request: HttpRequest object;
        id: id of product to be added to cart.

    Returns:
        HttpResponse object.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product, quantity=form.cleaned_data['quantity'], update_quantity=form.cleaned_data['update'])
    else:
        cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart_detail')


def cart_remove(request: HttpRequest, id: int) -> HttpResponse:
    """Remove product from user's shopping cart.

    Args:
        request: HttpRequest object;
        id: id of product to be removed from cart.

    Returns:
        HttpResponse object.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart_detail')


def order_cart(request: HttpRequest) -> HttpResponse:
    """Order products from user's shopping cart.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            address = Address.objects.create(
                index=form.cleaned_data['index'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                house_number=form.cleaned_data['house_number'],
                apartment_number=form.cleaned_data['apartment_number'],
            )
            order = Order.objects.create(
                buyer=request.user if request.user.id else None,
                address=address,
                status=OrderStatusChoices.CREATED,
            )
            for product in cart:
                ProductOrder.objects.create(
                    order=order,
                    product=product['products'],
                    price=product['total_price'],
                    quantity=product['quantity'],
                )
            cart.clear()
            return render(request, 'app_shop/cart/created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'app_shop/cart/create.html', {'cart': cart, 'form': form})


class OrderProductView(FormView):
    """FormView class for order product with specified id."""

    form_class = OrderForm
    success_url = '/'
    template_name = 'app_shop/cart/create.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Send a POST request for OrderProductView.

        Args:
            request: current request object;
            args: arguments for overriding;
            kwargs: keyword arguments for overriding.

        Returns:
            Response object.
        """
        form = OrderForm(request.POST)
        product = Product.objects.get(id=kwargs.get('id'))
        if form.is_valid():
            address = Address.objects.create(
                index=form.cleaned_data['index'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                house_number=form.cleaned_data['house_number'],
                apartment_number=form.cleaned_data['apartment_number'],
            )
            order = Order.objects.create(
                buyer=request.user if request.user.id else None,
                address=address,
                status=OrderStatusChoices.CREATED,
            )

            ProductOrder.objects.create(
                order=order,
                product=product,
                price=product.selling_price,
                quantity=1,
            )
            return render(request, 'app_shop/cart/created.html', {'order': order})
        return self.get(request, *args, **kwargs)
