from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import product
from cart.models import cart,order,account
@login_required

# Create your views here.
def addtocart(request,p):
    pr=product.objects.get(name=p)
    u=request.user
    try:
        c=cart.objects.get(product1=pr,user=u)
        if(c.quantity<c.product1.stock):
            c.quantity+=1
            c.save()
    except:
        c=cart.objects.create(product1=pr,user=u,quantity=1)
        c.save()
    return redirect('cart:cartview')
def cartview(request):
    total=0
    u=request.user
    try:
        c=cart.objects.filter(user=u)

        for i in c:
            total+=i.quantity*i.product1.price
    except:
        pass
      
    return render(request,'cart.html',{'c':c,'total':total})
def fullremove(request,p):
    pr=product.objects.get(name=p)
    u=request.user
    try:
        c=cart.objects.filter(product1=pr,user=u)
        c.delete()
    except:
        pass
    return redirect('cart:cartview')
def cartremove(request,p):
    pr=product.objects.get(name=p)
    u=request.user
    try:
        c=cart.objects.get(product1=pr,user=u)
        if(c.quantity>1):
            c.quantity-=1
            c.save()
        else:
            c.delete()
    except:
        pass
    return redirect('cart:cartview')
def orderform(request):
    if(request.method=="POST"):
        a = request.POST["a"]
        p = request.POST["p"]
        ac = request.POST["ac"]
        u = request.user
        c=cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product1.price
        acc=account.objects.get(acctnum=ac)
        if acc.amount>=total:
            acc.amount=acc.amount-total
            acc.save()

            for i in c:
                o = order.objects.create(user=u,product1=i.product1,address=a,phone=p,noofitems=i.quantity,order_status='paid')
                o.save()
                i.product1.stock = i.product1.stock-i.quantity
                i.product1.save()
            c.delete()
            msg="order placed successfully"
            return render(request,'orderdetail.html',{'msg':msg})
        else:
            msg="insufficient balance to place an order"
            return render(request,'orderdetail.html',{'msg':msg})
    return render(request,'orderform.html')
def orderview(request):
    u=request.user
    o=order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o})

