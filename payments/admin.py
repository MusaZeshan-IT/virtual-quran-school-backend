"""
The admin for the payment app
"""

from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    """The admin for the order model"""

    list_display = ("user", "status", "course", "amount", "transaction_id")


admin.site.register(Order, OrderAdmin)
