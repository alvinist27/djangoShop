"""Admin module of app_shop application."""

from django.contrib import admin

from app_shop.models import Product, Photo, Order, ProductOrder, Address, RightAccess, User, SellerData, Comment


class AddressAdmin(admin.ModelAdmin):
    """Class for admin view for Task objects."""

    list_filter = ('city',)
    list_display = ('city', 'street', 'house_number', 'apartment_number', 'index')


class CommentAdmin(admin.ModelAdmin):
    """Class for admin view for Comment objects."""

    list_display = ('user', 'product', 'text', 'user_rating', 'created')


class ProductOrderInline(admin.TabularInline):
    """Class for inline admin view for ProductOrder objects."""

    fk_name = 'order'
    model = ProductOrder


class OrderAdmin(admin.ModelAdmin):
    """Class for admin view for Order objects."""

    inlines = (ProductOrderInline,)
    list_filter = ('status',)
    list_display = ('created', 'status')


class PhotoInline(admin.TabularInline):
    """Class for inline admin view for Photo objects."""

    fk_name = 'product'
    model = Photo


class ProductAdmin(admin.ModelAdmin):
    """Class for admin view for Product objects."""

    inlines = (PhotoInline,)
    list_display = ('name', 'size', 'type', 'category', 'purchase_price', 'selling_price', 'quantity')
    list_filter = ('category', 'type')
    search_fields = ('name', 'description')


class RightAccessAdmin(admin.ModelAdmin):
    """Class for admin view for RightAccess objects."""

    list_display = ('id', 'name')


class SellerDataAdmin(admin.ModelAdmin):
    """Class for admin view for SellerData objects."""

    list_display = ('legal_name', 'user', 'type', 'email')
    list_filter = ('type',)


class UserAdmin(admin.ModelAdmin):
    """Class for admin view for User objects."""

    list_display = ('email', 'name', 'surname', 'birth_date', 'access')
    list_filter = ('access',)


admin.site.register(Address, AddressAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RightAccess, RightAccessAdmin)
admin.site.register(SellerData, SellerDataAdmin)
admin.site.register(User, UserAdmin)
