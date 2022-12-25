"""Module for app_lk views."""

import os

from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from app_lk.forms import ProductForm
from app_shop.models import Product, SellerData, Photo

PER_PAGE_RESULTS = 12

User = get_user_model()


class CreateProductView(FormView):
    """FormView class for creating products by seller."""

    form_class = ProductForm
    template_name = 'app_lk/product.html'

    def get_success_url(self) -> str:
        """Get success url of sending form to the same view.

        Returns:
            url path to follow after submitting the form.
        """
        return self.request.path

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Send a POST request for CreateProductView.

        Args:
            request: current request object;
            args: arguments for overriding;
            kwargs: keyword arguments for overriding.

        Returns:
            Response object.
        """
        super().post(request, *args, **kwargs)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            seller = SellerData.objects.get(user=User.objects.get(id=request.user.id))
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                type=form.cleaned_data['type'],
                category=form.cleaned_data['category'],
                purchase_price=form.cleaned_data['purchase_price'],
                selling_price=form.cleaned_data['selling_price'],
                size=form.cleaned_data['size'],
                quantity=form.cleaned_data['quantity'],
                seller=seller,
            )
            photos = request.FILES.getlist('photos')
            for photo in photos:
                file_path = default_storage.save(os.path.join('images', photo.name), photo)
                Photo.objects.create(file_path=file_path, product=product).save()
        return self.get(request)


def get_products_view(request: HttpRequest) -> HttpResponse:
    """Get seller's products.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    seller = SellerData.objects.get(user_id=request.user.id)
    products = Product.objects.filter(seller_id=seller.id)
    paginator = Paginator(products, PER_PAGE_RESULTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_lk/products_list.html', {'clothes': page_obj})


def update_product_view(request: HttpRequest, id: int) -> HttpResponse:
    """Update product by seller.

    Args:
        request: HttpRequest object;
        id: id of product to be updated.

    Returns:
        HttpResponse object.
    """
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.update_or_create(
                id=id,
                defaults={
                    'name': form.cleaned_data['name'],
                    'description': form.cleaned_data['description'],
                    'type': form.cleaned_data['type'],
                    'category': form.cleaned_data['category'],
                    'purchase_price': form.cleaned_data['purchase_price'],
                    'selling_price': form.cleaned_data['selling_price'],
                    'size': form.cleaned_data['size'],
                    'quantity': form.cleaned_data['quantity'],
                },
            )

            photos = request.FILES.getlist('photos')
            for photo in photos:
                file_path = default_storage.save(os.path.join('images', photo.name), photo)
                Photo.objects.create(file_path=file_path, product=product).save()
    else:
        form = ProductForm(instance=product)
    return render(request, 'app_lk/product.html', {'form': form, 'product_id': product.id})


def delete_product_view(request: HttpRequest, id: int) -> HttpResponse:
    """Remove product from user's shopping cart.

    Args:
        request: HttpRequest object;
        id: id of product to be removed.

    Returns:
        HttpResponse object.
    """
    product = Product.objects.get(id=id).delete()
    return render(request, 'app_lk/products_list.html', {'product': product})
