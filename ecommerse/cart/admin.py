from django.contrib import admin
from cart.models import cart
from cart.models import order
from cart.models import account
admin.site.register(cart)
admin.site.register(order)
admin.site.register(account)
# Register your models here.
