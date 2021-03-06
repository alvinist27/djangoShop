# Generated by Django 4.0.5 on 2022-07-23 21:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_shop', '0007_remove_order_username_alter_clothes_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='type',
            field=models.CharField(choices=[('Мужская', 'Мужская'), ('Женская', 'Женская'), ('Детская', 'Детская')], max_length=15, verbose_name='Тип'),
        ),
        migrations.CreateModel(
            name='ClothesReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(blank=True, null=True, verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cloth', to='app_shop.clothes', verbose_name='Товар')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
