from django import forms

from app_shop.choices import PRODUCT_TYPE_CHOICES, PRODUCT_CATEGORY_CHOICES, PRODUCT_SIZE_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    description = forms.CharField(max_length=300, widget=forms.Textarea(), required=False, label='Описание')
    type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES, label='Тип одежды')
    category = forms.ChoiceField(choices=PRODUCT_CATEGORY_CHOICES, label='Тип одежды')
    purchase_price = forms.FloatField(label='Цена закупки')
    selling_price = forms.FloatField(label='Цена продажи')
    size = forms.ChoiceField(choices=PRODUCT_SIZE_CHOICES, label='Размер')
    quantity = forms.IntegerField(label='Количество на складе')
