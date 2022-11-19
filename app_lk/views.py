from django.shortcuts import render
from django.views.generic import CreateView

from app_lk.forms import ProductForm
from app_shop.models import Product


# def create_products_view(request):
#     if request.method == 'POST':
#         # form = ProductForm(request.POST)
#         # if form.is_valid():
#         #     Product.objects.create(
#         #
#         #     )
#
#
#     else:
#         form = ProductForm()
#     return render(request, 'app_lk/add_product.html', {'form': form})


class MyModelCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'app_lk/add_product.html'

    # def form_valid(self, form):
    #     form.='string I want to save'
    #     #to save a clean string pass it between '' not ""
    #     form.instance.attr_2='a'
    #     return super().form_valid(form)
