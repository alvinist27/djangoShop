# Generated by Django 4.0.5 on 2022-06-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='images',
        ),
        migrations.AlterField(
            model_name='clothes',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='group',
            field=models.CharField(max_length=50, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(max_length=10, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='type',
            field=models.CharField(choices=[('Женская', 'Женская'), ('Мужская', 'Мужская'), ('Детская', 'Детская')], max_length=15, verbose_name='Тип'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images', verbose_name='Фото')),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.clothes')),
            ],
        ),
    ]
