from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class RightAccess(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Право доступа'
        verbose_name_plural = 'Права доступа'


class User(AbstractBaseUser):
    name = models.CharField(max_length=40, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    email = models.EmailField(max_length=50, verbose_name='Электронный адрес')
    access = models.ForeignKey(RightAccess, on_delete=models.DO_NOTHING, related_name='user', verbose_name='Права')

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, null=True, verbose_name='Описание')
    type = models.CharField(max_length=15, verbose_name='Тип одежды')
    category = models.CharField(max_length=50, verbose_name='Тип одежды')
    purchase_price = models.FloatField(verbose_name='Цена закупки')
    size = models.CharField(max_length=3, verbose_name='Размер')
    selling_price = models.FloatField(verbose_name='Цена продажи')
    quantity = models.IntegerField(verbose_name='Количество на складе')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Address(models.Model):
    index = models.IntegerField(verbose_name='Почтовый индекс')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=70, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Дом')
    apartment_number = models.IntegerField(verbose_name='Номер квартиры')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='buy', verbose_name='Покупатель')
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sell', verbose_name='Продавец')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='order', verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    status = models.IntegerField(verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='cloth', verbose_name='Товар')
    text = models.TextField(max_length=300, null=True, verbose_name='Текст отзыва')
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='clothes', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        db_table = 'app_version'
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

