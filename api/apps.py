"""Module with api configs."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration class for api application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
