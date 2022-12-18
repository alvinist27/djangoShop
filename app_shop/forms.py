from django import forms

from app_shop.choices import PRODUCT_CATEGORY_CHOICES
from app_shop.models import Comment

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductCategoryForm(forms.Form):
    select = forms.CharField(
        initial=PRODUCT_CATEGORY_CHOICES[0][0],
        widget=forms.RadioSelect(choices=PRODUCT_CATEGORY_CHOICES),
    )


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.Form):
    city = forms.CharField(max_length=50, label='Город')
    street = forms.CharField(max_length=70, label='Улица')
    house_number = forms.CharField(max_length=10, label='Дом')
    apartment_number = forms.IntegerField(label='Номер квартиры')
    index = forms.IntegerField(label='Почтовый индекс')


class DateFilterForm(forms.Form):
    start_date = forms.DateField(label='Дата начала периода')
    end_date = forms.DateField(label='Дата конца периода')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'user_rating')
