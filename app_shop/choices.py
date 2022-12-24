"""Module with choices using in forms and models."""

from django.db.models import IntegerChoices, TextChoices


class ProductTypeChoices(TextChoices):
    """Choices for selecting product type."""

    MEN = 'Мужская'
    WOMAN = 'Женская'
    CHILD = 'Детская'


class ProductCategoryChoices(TextChoices):
    """Choices for selecting product category."""

    ALL = 'Все товары'
    OUTERWEAR = 'Верхняя одежда'
    SHIRTS = 'Футболки'
    HOODIES = 'Толстовки'
    PANTS = 'Штаны'
    ACCESSORIES = 'Аксессуары'


class ProductSizeChoices(TextChoices):
    """Choices for selecting product size."""

    XS = 'XS'
    S = 'S'
    L = 'L'
    M = 'M'
    XL = 'XL'
    XXL = 'XXL'


class OrderStatusChoices(IntegerChoices):
    """Choices for tracking order statuses."""

    CREATED = 0, 'created'
    PAID = 1, 'paid'
    CONFIRMED = 2, 'confirmed'
    DELIVERED = 3, 'delivered'
