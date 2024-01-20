from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
import time
def register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'incorrect':'Username Already Taken'})
            elif User.objects.filter(email=email).exists():
                return render(request,'register.html',{'incorrect':'Email Already Taken'})
        
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                User.save
                return render(request,'register.html',{'correct':'User_Created Now Login To Continue'}) 
                
        else:
            return render(request,'register.html',{'incorrect':'Password doesent match'})
        
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:    
            return render(request,'login.html',{'incorrect':'Invalid Username Or Password'})
    else:    
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")
# Create your views here.
