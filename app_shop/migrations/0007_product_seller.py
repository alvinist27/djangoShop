# Generated by Django 4.1.2 on 2022-11-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0006_alter_comment_product_alter_productorder_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to='app_shop.sellerdata', verbose_name='Продавец'),
            preserve_default=False,
        ),
    ]
