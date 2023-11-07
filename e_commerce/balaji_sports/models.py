from django.db import models

# Create your models here.

catagory_choices=(("Simple","Simple"),("Master","Master"))
class Product(models.Model):
    catagory=models.CharField(max_length=10 , choices=catagory_choices , default="Simple")
    Simple_kit=models.BooleanField(default=False)
    simple_best_seller=models.BooleanField(default=False)
    Master_kit=models.BooleanField(default=False)
    master_best_seller=models.BooleanField(default=False)
    product_name=models.CharField(max_length=100,default='')
    product_desc=models.TextField(default='')
    product_img=models.ImageField(upload_to='pics/',default='')
    product_price=models.IntegerField(default="")
    product_sale=models.BooleanField(default=False)
    product_sale_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.product_name

