from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Category, Product, OrderItem, Order, Cart, CartItem, Customer
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PythonShopAdminSite(AdminSite):
    """Override Admin for manual shop management"""
    site_header = 'Python Shop Administration'
    index_title = 'Python Shop'
    site_title = 'Administration'
    
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if field.name != "id" 
                             or field.name != 'updated_at' or field.name != 'created_at' or field.name != 'deleted_at']
    exclude = ('deleted_at',)

admin_site = PythonShopAdminSite(name='shop_admin')

# Register your models here.
admin_site.register(Category)
admin_site.register(Product, ProductAdmin)
admin_site.register(Order)
admin_site.register(OrderItem)
admin_site.register(Cart)
admin_site.register(CartItem)
admin_site.register(Customer)
admin_site.register(User, UserAdmin)