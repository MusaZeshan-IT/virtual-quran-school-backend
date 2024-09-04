"""
The serializers for the contact app
"""

from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    """Contact message serializer"""

    class Meta:
        """The meta data for the serializer"""

        model = ContactMessage
        fields = ["name", "email_from", "subject", "message"]
