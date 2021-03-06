from django import forms
from django.utils.safestring import mark_safe
from .models import Order, ClothesReview

CHOICES = (
    ('1', 'Все товары'),
    ('2', 'Верхняя одежда'),
    ('3', 'Футболки'),
    ('4', 'Толстовки'),
    ('5', 'Штаны'),
    ('6', 'Аксессуары'),
)

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class RadioForm(forms.Form):
    select = forms.CharField(initial='1', widget=forms.RadioSelect(choices=CHOICES))


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'post_index', 'city']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ClothesReview
        fields = ['review_text', 'rating']
