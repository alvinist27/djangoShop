"""Module with app_users configs."""

from django.apps import AppConfig


class AppUsersConfig(AppConfig):
    """Configuration class for app_users application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_users'
