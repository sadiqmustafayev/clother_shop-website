# Generated by Django 5.0.3 on 2024-05-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, to='core.shopimage'),
        ),
    ]
