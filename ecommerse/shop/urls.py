"""
URL configuration for ecommerse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
app_name="shop"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.allcategories,name='allcategories'),
    path("regi",views.regi,name='register'),
    path("log",views.log,name='log'),
    path("shophome",views.shophome,name='shophome'),
    path("logout",views.user_logout,name='logout'),
    path("P/<p>",views.allproducts,name='allproducts'),
    path("Pd/<p>",views.productdetails,name='productdetails'),
  
]
