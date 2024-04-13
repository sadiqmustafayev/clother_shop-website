# Generated by Django 5.0.3 on 2024-04-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_blog_aforism_az_blog_aforism_en_blog_aforism_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_az',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_ru',
        ),
    ]
