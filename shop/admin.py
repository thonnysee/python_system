from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (Category, Product, OrderItem,
                     Order, Cart, CartItem, User)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


class PythonShopAdminSite(AdminSite):
    """Override Admin for admin shop"""
    site_header = 'Python Shop Administration'
    index_title = 'Python Shop'
    site_title = 'Administration'


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields
                    if field.name != "id" or field.name != 'updated_at' or
                    field.name != 'created_at' or field.name != 'deleted_at'
                    ]
    exclude = ('deleted_at',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('deleted_at',)


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'firstname']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {'fields': ('firstname', 'lastname', 'second_lastname')}
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin_site = PythonShopAdminSite()

# Register your models here.
admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Order)
admin_site.register(OrderItem)
admin_site.register(Cart)
admin_site.register(CartItem)
admin_site.register(User, UserAdmin)
