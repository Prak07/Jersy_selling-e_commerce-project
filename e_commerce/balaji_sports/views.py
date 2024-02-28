from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *
# Create your views here.


def index(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(simple_best_seller=True).count()
    countm=Product.objects.all().filter(master_best_seller=True).count()
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        global items , cart_total
        items=order.orderitem_set.all()
        cart_total=order.get_cart_total
    else:
        items=[]
        cart_total=0
    return render(request,"index.html",{"products":products,"count":count,"countm":countm,"cart_items":items,"total":cart_total})
    

def Master(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(simple_best_seller=True).count()
    countm=Product.objects.all().filter(master_best_seller=True).count()
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        global items , cart_total
        items=order.orderitem_set.all()
        cart_total=order.get_cart_total
    else:
        items=[]
        cart_total=0
    products=Product.objects.all()
    count=Product.objects.all().filter(Master_kit=True).count()
    return render(request,"MasterKits.html",{"products":products,"count":count,"cart_items":items,"total":cart_total})


def Simple(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(simple_best_seller=True).count()
    countm=Product.objects.all().filter(master_best_seller=True).count()
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        global items , cart_total
        items=order.orderitem_set.all()
        cart_total=order.get_cart_total
    else:
        items=[]
        cart_total=0
    products=Product.objects.all()
    count=Product.objects.all().filter(Simple_kit=True).count()
    return render(request,"SimpleKits.html",{"products":products,"count":count,"cart_items":items,"total":cart_total})

def AboutUs(request):
    return render(request,"about.html")

def ContactUS(request):
    return render(request,"index.html")

def TrackingStatus(request):
    return render(request,"index.html")

def Search(request):
    return render(request,"index.html")

def ProductView(request,prodid):
    products=Product.objects.all()
    count=Product.objects.all().filter(simple_best_seller=True).count()
    countm=Product.objects.all().filter(master_best_seller=True).count()
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        global items , cart_total
        items=order.orderitem_set.all()
        cart_total=order.get_cart_total
    else:
        items=[]
        cart_total=0
    Prod=Product.objects.filter(id=prodid)
    return render(request,"productview.html",{"product":Prod[0],"cart_items":items,"total":cart_total})

def Checkout(request):
    return render(request,"index.html")

def Cart(request):
    return render(request,"cart.html")

def login(request):
    return render(request,"index.html")


def updateitem(request):
    data=json.loads(request.body)
    productid=data['Product_id']
    action=data['action']
    print(productid,action)
    customer=request.user
    product=Product.objects.get(id=productid)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order_item=order,product=product)
    if action=='plus':
        orderItem.quantity+=1
    elif action=='minus':
        orderItem.quantity-=1    
    
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('item was added',safe=False)
