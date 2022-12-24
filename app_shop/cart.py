"""Module containing the basic logic of the shopping cart."""

from decimal import Decimal
from typing import Optional, Iterator

from django.conf import settings
from django.http import HttpRequest

from app_shop.models import Product


class Cart:
    """Shopping cart class."""

    def __init__(self, request: HttpRequest) -> None:
        """Initializing the shopping cart.

        Args:
            request: HttpRequest object.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: Product, quantity: Optional[int] = 1, update_quantity: Optional[bool] = False) -> None:
        """Add a product to the cart or update its quantity.

        Args:
            product: Product class instance to be added to the cart;
            quantity: quantity of product items to be added;
            update_quantity: it is necessary to update the quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.selling_price),
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self) -> None:
        """Update cart session."""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product: Product) -> None:
        """Remove product from the cart.

        Args:
            product: Product class instance to be removed from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self) -> Iterator:
        """Iterator object of Cart class."""
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)]['products'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self) -> int:
        """Get the length of a Cart object.

        Returns:
            Total number of products in shopping cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self) -> int:
        """Get total price of all products in the Cart .

        Returns:
            Total price of products in shopping cart.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self) -> None:
        """Clear shopping cart."""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
