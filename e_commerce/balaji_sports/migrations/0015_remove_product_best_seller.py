# Generated by Django 4.2.3 on 2023-09-24 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balaji_sports', '0014_product_best_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='best_seller',
        ),
    ]
