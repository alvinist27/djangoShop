"""Module with choices using in forms and models."""

from django.db.models import IntegerChoices, TextChoices


class ProductTypeChoices(TextChoices):
    """Choices for selecting product type."""

    MEN = 'Мужская', 'Мужская'
    WOMAN = 'Женская', 'Женская'
    CHILD = 'Детская', 'Детская'


class ProductCategoryChoices(TextChoices):
    """Choices for selecting product category."""

    ALL = 'Все товары', 'Все товары'
    OUTERWEAR = 'Верхняя одежда', 'Верхняя одежда'
    SHIRTS = 'Футболки', 'Футболки'
    HOODIES = 'Толстовки', 'Толстовки'
    PANTS = 'Штаны', 'Штаны'
    ACCESSORIES = 'Аксессуары', 'Аксессуары'


class ProductSizeChoices(TextChoices):
    """Choices for selecting product size."""

    XS = 'XS', 'XS'
    S = 'S', 'S'
    L = 'L', 'L'
    M = 'M', 'M'
    XL = 'XL', 'XL'
    XXL = 'XXL', 'XXL'


class OrderStatusChoices(IntegerChoices):
    """Choices for tracking order statuses."""

    CREATED = 0, 'Создан'
    PAID = 1, 'Оплачен'
    CONFIRMED = 2, 'Подтверждён'
    DELIVERED = 3, 'Доставлен'


class UserGroupChoices(TextChoices):
    """Choices for selecting group of user in registration process."""

    SELLER = 'Продавец', 'Продавец'
    CUSTOMER = 'Покупатель', 'Покупатель'


class OrganizationTypeChoices(TextChoices):
    """Choices for selecting type of seller organization in registration process."""

    IP = 'ИП', 'ИП'
    OOO = 'ООО', 'ООО'
    OAO = 'ОАО', 'ОАО'
    ZAO = 'ЗАО', 'ЗАО'
    PAO = 'ПАО', 'ПАО'
