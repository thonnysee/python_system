# Generated by Django 2.2.7 on 2019-11-29 23:49

from django.db import migrations
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', shop.models.UserManager()),
            ],
        ),
    ]