"""Module with app_shops configs."""

from django.apps import AppConfig


class AppShopConfig(AppConfig):
    """Configuration class for app_shops application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_shop'
