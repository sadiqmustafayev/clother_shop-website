# Generated by Django 5.0.3 on 2024-05-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_product_color_az_product_color_en_product_color_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
