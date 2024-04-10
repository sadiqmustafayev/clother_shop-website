# Generated by Django 5.0.3 on 2024-04-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_currency_code_alter_currency_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(default=1, max_length=3, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
