from django.contrib import admin

from app_shop.models import Product, Photo, Order, ProductOrder


class PhotoInline(admin.TabularInline):
    fk_name = 'product'
    model = Photo


class OrderClothInline(admin.TabularInline):
    fk_name = 'order'
    model = ProductOrder


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ['name', 'size', 'type', 'category', 'purchase_price', 'selling_price', 'quantity']
    list_filter = ['category', 'type']
    search_fields = ['name', 'description']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderClothInline]
    list_filter = ['status']
    list_display = ['created', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
