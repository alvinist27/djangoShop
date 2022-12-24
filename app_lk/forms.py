"""Module with app_lk forms."""

from django import forms

from app_shop.models import Product


class ProductForm(forms.ModelForm):
    """Form for adding product by the seller."""

    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Фото товара')
    description = forms.CharField(max_length=300, widget=forms.Textarea(), required=False, label='Описание')

    class Meta:
        """Class with meta information of ProductForm."""

        model = Product
        fields = ('name', 'description', 'type', 'category', 'size', 'purchase_price', 'selling_price', 'quantity')
