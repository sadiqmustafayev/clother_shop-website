# Generated by Django 5.0.3 on 2024-05-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_myuser_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]