# Generated by Django 2.2.7 on 2019-11-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191113_0419'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Area',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='area',
            new_name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='special_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default='https://aliceasmartialarts.com/wp-content/uploads/2017/04/default-image.jpg'),
        ),
    ]
