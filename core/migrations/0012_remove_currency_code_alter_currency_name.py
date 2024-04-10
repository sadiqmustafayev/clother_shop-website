# Generated by Django 5.0.3 on 2024-04-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_product_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='code',
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
