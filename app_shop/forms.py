"""Module with app_shop forms."""

from django import forms

from app_shop.choices import ProductCategoryChoices
from app_shop.models import Comment

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductCategoryForm(forms.Form):
    """Form for selecting the displayed product category."""

    select = forms.CharField(
        initial=ProductCategoryChoices.ALL,
        widget=forms.RadioSelect(choices=ProductCategoryChoices.choices),
    )


class CartAddProductForm(forms.Form):
    """Form for adding product to the shopping cart."""

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.Form):
    """Form for product ordering."""

    city = forms.CharField(max_length=50, label='Город')
    street = forms.CharField(max_length=70, label='Улица')
    house_number = forms.CharField(max_length=10, label='Дом')
    apartment_number = forms.IntegerField(label='Номер квартиры')
    index = forms.IntegerField(label='Почтовый индекс')


class DateFilterForm(forms.Form):
    """Form for date filtering."""

    start_date = forms.DateField(label='Дата начала периода')
    end_date = forms.DateField(label='Дата конца периода')


class CommentForm(forms.ModelForm):
    """Form for adding customer reviews."""

    class Meta:
        """Class with meta information of CommentForm."""

        model = Comment
        fields = ('text', 'user_rating')
