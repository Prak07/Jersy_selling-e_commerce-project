from django.db import models
from django.contrib.auth.models import User
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

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False , null = True ,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=0
        for item in orderitems:
            total+=item.quantity
        return total
    @property
    def get_cart_price_total(self):
        orderitems=self.orderitem_set.all()
        total=0
        for item in orderitems:
            total+=item.get_total
        return total
    

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order_item=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.product.product_name
    
    @property
    def get_total(self):
        total=self.product.product_price * self.quantity
        return total
        

    