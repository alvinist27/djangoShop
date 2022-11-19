from django.urls import path

from app_lk.views import MyModelCreateView

urlpatterns = [
    # path('', [], name='lk_read'),
    path('add_product', MyModelCreateView.as_view(), name='lk_create'),
    # path('delete_product', RegistrationView.as_view(), name='lk_delete'),
    # path('update_product', RegistrationView.as_view(), name='lk_update'),
]
