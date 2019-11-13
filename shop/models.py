from django.db import models
from django_paranoid.models import ParanoidModel
import uuid
from django.template.defaultfilters import slugify
from django.conf import settings


# Create your models here.
class Area(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=264, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(ParanoidModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    summary = models.CharField(max_length=264, null=True)
    description = models.CharField(max_length=264, null=True)
    sku = models.CharField(max_length=50, unique=True, null=True)
    price = models.FloatField(default=0.00)
    is_active = models.BooleanField(default=True)
    product_type = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    
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