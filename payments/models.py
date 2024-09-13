"""
Models for the payment app
"""

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """The model for the order"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="pending")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
