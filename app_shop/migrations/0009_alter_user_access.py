# Generated by Django 4.1.2 on 2022-10-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0008_alter_user_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='app_shop.rightaccess', verbose_name='Права'),
        ),
    ]
