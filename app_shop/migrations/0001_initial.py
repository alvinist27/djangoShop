# Generated by Django 4.1.2 on 2022-11-02 20:29

from typing import List

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies: List = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=40, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_date', models.DateField(null=True, verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='Почтовый индекс')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=70, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Дом')),
                ('apartment_number', models.IntegerField(null=True, verbose_name='Номер квартиры')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('status', models.IntegerField(verbose_name='Статус заказа')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='app_shop.address', verbose_name='Адрес')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buy', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sell', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='Описание')),
                ('type', models.CharField(max_length=15, verbose_name='Тип одежды')),
                ('category', models.CharField(max_length=50, verbose_name='Тип одежды')),
                ('purchase_price', models.FloatField(verbose_name='Цена закупки')),
                ('size', models.CharField(max_length=3, verbose_name='Размер')),
                ('selling_price', models.FloatField(verbose_name='Цена продажи')),
                ('quantity', models.IntegerField(verbose_name='Количество на складе')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='RightAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Право доступа',
                'verbose_name_plural': 'Права доступа',
            },
        ),
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='Название категории')),
                ('INN', models.IntegerField(verbose_name='ИНН')),
                ('reg_date', models.DateField(verbose_name='Дата регистрации организации')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Электронный адрес организации')),
                ('legal_name', models.CharField(max_length=50, verbose_name='Юридическое название')),
                ('legal_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='app_shop.address', verbose_name='Юридический адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='app_shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
                'db_table': 'app_version',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.ImageField(upload_to='images', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app_shop.product')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300, null=True, verbose_name='Текст отзыва')),
                ('user_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cloth', to='app_shop.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='access',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='app_shop.rightaccess', verbose_name='Права'),
        ),
        migrations.AddConstraint(
            model_name='productorder',
            constraint=models.UniqueConstraint(fields=('order', 'product'), name='product_in_order'),
        ),
    ]
