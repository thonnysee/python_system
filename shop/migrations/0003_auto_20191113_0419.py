# Generated by Django 2.2.7 on 2019-11-13 04:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20191113_0412'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Areas',
            new_name='Area',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
