from django.contrib import admin
from .models import Area, Product, OrderItem, Order

# Register your models here.
admin.site.register(Area)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)