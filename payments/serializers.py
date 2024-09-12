"""
The serializers for the payment app
"""

from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """The serializer for the order model"""

    class Meta:
        """The meta data for the serializer"""

        model = Order
        fields = ["id", "status", "amount", "transaction_id"]
