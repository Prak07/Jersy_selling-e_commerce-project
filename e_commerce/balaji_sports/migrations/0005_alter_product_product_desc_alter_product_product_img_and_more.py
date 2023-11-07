# Generated by Django 4.2.3 on 2023-09-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balaji_sports', '0004_alter_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='', upload_to='media/pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
