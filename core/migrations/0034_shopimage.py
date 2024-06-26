# Generated by Django 5.0.3 on 2024-05-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_faq_remove_blog_slug_az_remove_blog_slug_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'ShopImage',
                'verbose_name_plural': 'ShopImage',
            },
        ),
    ]
