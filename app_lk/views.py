import os

from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import render

from app_lk.forms import ProductForm
from app_shop.models import Product, SellerData, User, Photo


def create_product_view(request):
    if request.method == 'POST':
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
    else:
        form = ProductForm()
    return render(request, 'app_lk/product.html', {'form': form})


def get_products_view(request):
    seller = SellerData.objects.get(user_id=request.user.id)
    products = Product.objects.filter(seller_id=seller.id)
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_lk/products_list.html', {'clothes': page_obj})


def update_product_view(request, id):
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


def delete_product_view(request, id):
    product = Product.objects.get(id=id).delete()
    return render(request, 'app_lk/products_list.html', {'product': product})