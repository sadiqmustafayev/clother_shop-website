# Generated by Django 5.0.3 on 2024-05-02 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_shopcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color_az',
            field=models.ManyToManyField(null=True, to='core.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_en',
            field=models.ManyToManyField(null=True, to='core.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_ru',
            field=models.ManyToManyField(null=True, to='core.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency_az',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency'),
        ),
    ]