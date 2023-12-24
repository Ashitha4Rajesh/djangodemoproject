from django.shortcuts import render
from shop.models import category,product
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your views here.


def regi(request):
    if(request.method=="POST"):
        u = request.POST["u"]
        p = request.POST["p"]
        cp = request.POST["cp"]
        e = request.POST["e"]
        if(p==cp):

            b = user.objects.create_user(username=u,password=p,email=e)
            b.save()
            return allcategories(request)
    return render(request,'regi.html')
def log(request):
    if(request.method=="POST"):
        username = request.POST["u"]
        password = request.POST["p"]
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return shophome(request)
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')
def shophome(request):
    return render(request,'shophome.html')
@login_required
def user_logout(request):
    logout(request)
    return log(request)
def allcategories(request):
    b = category.objects.all()
    return render(request,"category.html",{"categories":b})
def allproducts(request,p):
    c = category.objects.get(name=p)
    p = product.objects.filter(category1=c)
    return render(request,"product.html",{"c":c,'p':p})
def productdetails(request,p):
    p = product.objects.get(name=p)
    return render(request,"productdetails.html",{"p":p})