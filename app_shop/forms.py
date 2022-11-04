from django import forms

from app_shop.choices import PRODUCT_CATEGORY_CHOICES

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductCategoryForm(forms.Form):
    select = forms.CharField(
        initial=PRODUCT_CATEGORY_CHOICES[0][0],
        widget=forms.RadioSelect(choices=PRODUCT_CATEGORY_CHOICES),
    )
