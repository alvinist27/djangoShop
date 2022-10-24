# Generated by Django 4.1.2 on 2022-10-24 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='Название категории')),
                ('INN', models.IntegerField(verbose_name='ИНН')),
                ('reg_date', models.DateField(verbose_name='Дата регистрации организации')),
                ('legal_name', models.CharField(max_length=50, verbose_name='Юридическое название')),
                ('legal_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='app_shop.address', verbose_name='Юридический адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
    ]