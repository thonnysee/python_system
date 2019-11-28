"""
shop.models.py
====================================
The models of the shop app

"""

from django.db import models
from django_paranoid.models import ParanoidModel
import uuid
from django.template.defaultfilters import slugify
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom Model of User for Shop """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=254)
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    second_lastname = models.CharField(max_length=254)
    birthday = models.DateField(null=True)
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    lang = models.CharField(max_length=4, default='en')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Category(ParanoidModel):
    """
    Stores products category, related to :model:`shop.Product`.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=264, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        """Adds order by name to model"""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ["-name"]

    def save(self, *args, **kwargs):
        """Adds a slug of the category based on the name"""
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        """Return Category name"""
        return self.name


class Product(ParanoidModel):
    """
    Stores products with stock control, related to :model:`shop.Category`.
    """
    u = 'https://aliceasmartialarts.com/wp-content/uploads/2017/04/ \
        + default-image.jpg'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    summary = models.CharField(max_length=264, null=True)
    description = models.CharField(max_length=264, null=True)
    sku = models.CharField(max_length=50, unique=True, null=True)
    price = models.FloatField(default=0.00)
    special_price = models.FloatField(default=0.00)
    product_type = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, related_name='category')
    url = models.URLField(max_length=200, default=u)
    is_active = models.BooleanField(default=True)

    @property
    def has_stock(self):
        return self.stock > 0

    def save(self, *args, **kwargs):
        """Adds slug of the Product name"""
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        """Return Product name"""
        return self.sku


class Order(ParanoidModel):
    """Creates the purchase order/invoice of the Customer,
    related to :model:`auth.User`."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.PositiveIntegerField(null=False)
    total = models.FloatField(default=0.00)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="pending")


class OrderItem(ParanoidModel):
    """
    Stores the relation many to many of Products and Orders,
    related to :model:`shop.Products`, :model:`shop.Order`.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,
                                 null=True, related_name='order')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   null=True, related_name='product')
    unit_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)


class Cart(ParanoidModel):
    """Stores the relation cart and customer related to :model:`auth.User`."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE, null=True,
                                related_name='user')
    state = models.CharField(max_length=50, default='active')


class CartItem(ParanoidModel):
    """
    Stores the relation many to many of Products and Carts if stock
    is available (Product.stock >= 1), related to :model:`shop.Products`,
    :model:`shop.Carts`.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,
                                related_name='cart')
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)
