"""
shop_seeder.py
===============
Module to populate the models of the app shop
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_project.settings')
import django
django.setup()
from random import randint
from shop.models import Product, Category
from faker import Faker
from django.template.defaultfilters import slugify
import requests


fake = Faker()
url = 'https://picsum.photos/v2/list'
json = requests.get(url).json()


def products_seeder(times=5):
    """
    Populate the model Product with fake data
    Parameters
    ----------
    times
        Number of new data sets for the model
    """
    for seed in range(times):
        name = "producto_" + str(seed)
        summary = fake.paragraph(nb_sentences=3, variable_nb_sentences=True,
                                 ext_word_list=None)
        description = fake.paragraphs(nb=1, ext_word_list=None)
        sku = fake.msisdn()
        price = fake.pydecimal(left_digits=None, right_digits=None,
                               positive=True, min_value=0, max_value=None)
        special_price = fake.pydecimal(left_digits=None, right_digits=None,
                                       positive=True, min_value=0,
                                       max_value=None)
        product_type = "Muebles"
        slug = "mueble-" + str(seed)
        stock = randint(0, 100)
        url = json[seed]['download_url']
        category = Category.objects.first()
        if category is None:
            category = Category(name="Muebles Hogar",
                                description="Categoria de Muebles",
                                slug=slugify("Muebles Hogar"))
            category.save()
        product = Product.objects.get_or_create(
            name=name,
            summary=summary,
            description=description,
            sku=sku,
            price=price,
            product_type=product_type,
            slug=slug,
            stock=stock,
            category=category,
            special_price=special_price,
            url=url
        )[0]
        product.save()


if __name__ == "__main__":
    products_seeder(20)
