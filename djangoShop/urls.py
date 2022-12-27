"""Module for djangoShop project routing."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app_users.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statistics/', admin_site.urls),
    path('api/', include('api.urls')),
    path('', include('app_shop.urls')),
    path('lk/', include('app_lk.urls')),
    path('users/', include('app_users.urls')),
    path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
