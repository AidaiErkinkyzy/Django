# Generated by Django 5.0.7 on 2024-07-12 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='food_images')),
                ('gram', models.IntegerField(default=0, verbose_name='Граммовка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='product.category')),
            ],
        ),
    ]
