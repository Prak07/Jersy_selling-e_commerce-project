from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(simple_best_seller=True).count()
    countm=Product.objects.all().filter(master_best_seller=True).count()
    return render(request,"index.html",{"products":products,"count":count,"countm":countm})
    

def Master(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(Master_kit=True).count()
    return render(request,"MasterKits.html",{"products":products,"count":count})


def Simple(request):
    products=Product.objects.all()
    count=Product.objects.all().filter(Simple_kit=True).count()
    return render(request,"SimpleKits.html",{"products":products,"count":count})

def AboutUs(request):
    return render(request,"about.html")

def ContactUS(request):
    return render(request,"index.html")

def TrackingStatus(request):
    return render(request,"index.html")

def Search(request):
    return render(request,"index.html")

def ProductView(request,prodid):
    Prod=Product.objects.filter(id=prodid)
    return render(request,"productview.html",{"product":Prod[0]})

def Checkout(request):
    return render(request,"index.html")

def Cart(request):
    return render(request,"index.html")

def login(request):
    return render(request,"index.html")
