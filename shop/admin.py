from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Category, Product, OrderItem, Order, Cart, CartItem, Customer
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PythonShopAdminSite(AdminSite):
    site_header = 'Python Shop Administration'
    index_title = 'Python Shop'
    site_title = 'Administration'

admin_site = PythonShopAdminSite(name='shop_admin')

# Register your models here.
admin_site.register(Category)
admin_site.register(Product)
admin_site.register(Order)
admin_site.register(OrderItem)
admin_site.register(Cart)
admin_site.register(CartItem)
admin_site.register(Customer)
admin_site.register(User, UserAdmin)