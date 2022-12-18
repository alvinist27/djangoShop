from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_shop.choices import PRODUCT_CATEGORY_CHOICES, PRODUCT_SIZE_CHOICES, PRODUCT_TYPE_CHOICES


class Address(models.Model):
    index = models.IntegerField(verbose_name='Почтовый индекс')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=70, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Дом')
    apartment_number = models.IntegerField(null=True, verbose_name='Номер квартиры')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        address = f'{self.city}, {self.street}, {self.house_number}'
        if self.apartment_number:
            address += f', {self.apartment_number}'
        return address


class RightAccess(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Право доступа'
        verbose_name_plural = 'Права доступа'

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique auth identifier"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        admin_access_id = 5
        extra_fields.setdefault('access_id', admin_access_id)
        if extra_fields.get('access_id') != admin_access_id:
            raise ValueError(_('Superuser must admin access right.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=40, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес')
    access = models.ForeignKey(
        RightAccess, on_delete=models.DO_NOTHING, related_name='access', verbose_name='Права', default=3,
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        if self.access.id >= 5:
            return True
        return False

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class SellerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    type = models.CharField(max_length=5, verbose_name='Название категории')
    INN = models.IntegerField(verbose_name='ИНН')
    reg_date = models.DateField(verbose_name='Дата регистрации организации')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес организации')
    legal_name = models.CharField(max_length=50, verbose_name='Юридическое название')
    legal_address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='seller', verbose_name='Юридический адрес',
    )

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'

    def __str__(self):
        return self.legal_name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, null=True, verbose_name='Описание')
    type = models.CharField(max_length=15, verbose_name='Тип одежды', choices=PRODUCT_TYPE_CHOICES)
    category = models.CharField(max_length=50, verbose_name='Категория', choices=PRODUCT_CATEGORY_CHOICES)
    purchase_price = models.FloatField(verbose_name='Цена закупки')
    size = models.CharField(max_length=3, verbose_name='Размер', choices=PRODUCT_SIZE_CHOICES)
    selling_price = models.FloatField(verbose_name='Цена продажи')
    quantity = models.IntegerField(verbose_name='Количество на складе')
    seller = models.ForeignKey(SellerData, on_delete=models.DO_NOTHING, related_name='seller', verbose_name='Продавец')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='buy', verbose_name='Покупатель')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='order', verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    status = models.IntegerField(verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='product', verbose_name='Товар')
    text = models.TextField(max_length=300, null=True, verbose_name='Текст отзыва')
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cloth_order', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cloth_product', verbose_name='Товар')
    price = models.FloatField(verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='product_in_order'),
        ]
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file_path = models.ImageField(upload_to='images', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
