"""Module for app_shop models."""

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_shop.choices import OrderStatusChoices, ProductSizeChoices, ProductCategoryChoices, ProductTypeChoices


class Address(models.Model):
    """Model for Address entities."""

    index = models.IntegerField(verbose_name='Почтовый индекс')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=70, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Дом')
    apartment_number = models.IntegerField(null=True, blank=True, verbose_name='Номер квартиры')

    class Meta:
        """Class with meta information of Address model."""

        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self) -> str:
        """Return string representation of the Address model.

        Returns:
            Address string received from Address object.
        """
        address = f'{self.city}, {self.street}, {self.house_number}'
        if self.apartment_number:
            address += f', {self.apartment_number}'
        return address


class RightAccess(models.Model):
    """Model for RightAccess entities."""

    name = models.CharField(max_length=70, verbose_name='Название категории')

    class Meta:
        """Class with meta information of RightAccess model."""

        verbose_name = 'Право доступа'
        verbose_name_plural = 'Права доступа'

    def __str__(self) -> str:
        """Return string representation of the RightAccess model.

        Returns:
            Name of the RightAccess object.
        """
        return self.name


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique auth identifier."""

    def create_user(self, email: str, password: str, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        admin_access_id = 5
        extra_fields.setdefault('access_id', admin_access_id)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('access_id') != admin_access_id:
            raise ValueError(_('Superuser must admin access right.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""

    name = models.CharField(max_length=40, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес')
    access = models.ForeignKey(
        RightAccess, on_delete=models.SET_NULL, null=True, related_name='access', verbose_name='Права', default=3,
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        """Class with meta information of User model."""

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        """Return string representation of the SellerData model.

        Returns:
            Email of the User object.
        """
        return self.email

    @property
    def is_staff(self) -> bool:
        """Designates whether this user can access the admin site.

        Returns:
            Boolean value determining if the user is a staff.
        """
        if self.access.id >= 5:
            return True
        return False


class SellerData(models.Model):
    """Model for SellerData entities."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    type = models.CharField(max_length=5, verbose_name='Название категории')
    INN = models.IntegerField(verbose_name='ИНН')
    reg_date = models.DateField(verbose_name='Дата регистрации организации')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес организации')
    legal_name = models.CharField(max_length=50, verbose_name='Юридическое название')
    legal_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name='seller', verbose_name='Юридический адрес',
    )

    class Meta:
        """Class with meta information of SellerData model."""

        verbose_name = 'Данные продавца'
        verbose_name_plural = 'Данные продавцов'

    def __str__(self) -> str:
        """Return string representation of the SellerData model.

        Returns:
            Legal_name of the SellerData object.
        """
        return self.legal_name


class Product(models.Model):
    """Model for Product entities."""

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    type = models.CharField(max_length=15, verbose_name='Тип одежды', choices=ProductTypeChoices.choices)
    category = models.CharField(max_length=50, verbose_name='Категория', choices=ProductCategoryChoices.choices)
    purchase_price = models.FloatField(verbose_name='Цена закупки')
    size = models.CharField(max_length=3, verbose_name='Размер', choices=ProductSizeChoices.choices)
    selling_price = models.FloatField(verbose_name='Цена продажи')
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество на складе')
    seller = models.ForeignKey(SellerData, on_delete=models.CASCADE, related_name='seller', verbose_name='Продавец')

    class Meta:
        """Class with meta information of Product model."""

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        """Return string representation of the Product model.

        Returns:
            Name of the Product object.
        """
        return self.name


class Order(models.Model):
    """Model for Order entities."""

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    status = models.IntegerField(verbose_name='Статус заказа', choices=OrderStatusChoices.choices)
    buyer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='buy', verbose_name='Покупатель',
    )
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name='order', verbose_name='Адрес',
    )

    class Meta:
        """Class with meta information of Order model."""

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        """Return string representation of the Order model.

        Returns:
            Number of the Order object.
        """
        return f'Заказ № {self.id}'


class Comment(models.Model):
    """Model for Comment entities."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', verbose_name='Товар')
    text = models.TextField(verbose_name='Текст отзыва')
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='user', verbose_name='Пользователь',
    )

    class Meta:
        """Class with meta information of Comment model."""

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductOrder(models.Model):
    """Model for ProductOrder entities."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cloth_order', verbose_name='Заказ')
    price = models.FloatField(verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='cloth_product', verbose_name='Товар',
    )

    class Meta:
        """Class with meta information of ProductOrder model."""

        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='product_in_order'),
        ]
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class Photo(models.Model):
    """Model for Photo entities."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file_path = models.ImageField(upload_to='images', verbose_name='Фото')

    class Meta:
        """Class with meta information of Photo model."""

        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
