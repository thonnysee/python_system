from django.db import models
from django_paranoid.models import ParanoidModel
import uuid
from django.template.defaultfilters import slugify
from django.conf import settings


# Create your models here.
class Category(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=264, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, default="")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    summary = models.CharField(max_length=264, null=True)
    description = models.CharField(max_length=264, null=True)
    sku = models.CharField(max_length=50, unique=True, null=True)
    price = models.FloatField(default=0.00)
    special_price = models.FloatField(default=0.00)
    product_type = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=200,default="https://aliceasmartialarts.com/wp-content/uploads/2017/04/default-image.jpg")
    is_active = models.BooleanField(default=True) 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Order(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.PositiveIntegerField(unique=True, null=True)
    total = models.FloatField(default=0.00)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="pending")
    
    def __str__(self):
        return str(self.order_number)
    
class OrderItem(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    unit_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)