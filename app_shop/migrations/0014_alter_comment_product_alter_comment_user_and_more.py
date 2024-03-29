# Generated by Django 4.1.2 on 2022-12-24 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0013_alter_order_status_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app_shop.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='app_shop.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buy', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='app_shop.sellerdata', verbose_name='Продавец'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cloth_product', to='app_shop.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='sellerdata',
            name='legal_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to='app_shop.address', verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='access', to='app_shop.rightaccess', verbose_name='Права'),
        ),
    ]
