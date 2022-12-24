"""Module with choices using in forms and models."""

PRODUCT_TYPE_CHOICES = (
    ('Мужская', 'Мужская'),
    ('Женская', 'Женская'),
    ('Детская', 'Детская'),
)

PRODUCT_CATEGORY_CHOICES = (
    ('Все товары', 'Все товары'),
    ('Верхняя одежда', 'Верхняя одежда'),
    ('Футболки', 'Футболки'),
    ('Толстовки', 'Толстовки'),
    ('Штаны', 'Штаны'),
    ('Аксессуары', 'Аксессуары'),
)

PRODUCT_SIZE_CHOICES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('L', 'L'),
    ('M', 'M'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
)


class OrderStatus:
    """Enum for tracking order statuses."""

    created = 0
    paid = 1
    confirmed = 2
    delivered = 3
