import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_project.settings')
import django
django.setup()

from random import randint
from shop.models import Product, Area, Order, OrderItem
from faker import Faker

fake = Faker()

def seeder(times=5):
    for seed in range(times):
        name = "mueble_" + str(seed)
        summary = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        description = fake.paragraphs(nb=1, ext_word_list=None)
        sku = fake.msisdn()
        price = fake.pydecimal(left_digits=None, right_digits=None, positive=True, min_value=0, max_value=None)
        product_type = "Muebles"
        slug = "mueble-" + str(seed)
        stock = randint(0, 100)
        area = Area.objects.first()
        product = Product.objects.get_or_create(
            name = name,
            summary = summary,
            description = description,
            sku = sku,
            price = price,
            product_type = product_type,
            slug = slug,
            stock = stock,
            area = area
        )[0]
        product.save()
        
if __name__ == "__main__":
    seeder(30)
        

