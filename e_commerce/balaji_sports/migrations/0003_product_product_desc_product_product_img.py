# Generated by Django 4.2.3 on 2023-09-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balaji_sports', '0002_product_product_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
