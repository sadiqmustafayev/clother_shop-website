# Generated by Django 5.0.3 on 2024-04-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(default='USD', max_length=3, unique=True),
        ),
    ]
