"""
The serializers for the contact app
"""

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    """Contact message serializer"""

    class Meta:
        """The meta data for the serializer"""

        model = ContactMessage
        fields = ["id", "name", "email_from", "subject", "message", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        # Save the contact message to the database
        contact_message = ContactMessage.objects.create(**validated_data)

        # Send an email notification
        subject = f"New Contact Message: {validated_data['subject']}"
        message = f"""
        You have received a new message from {validated_data['name']} <{validated_data['email_from']}>.

        Subject: {validated_data['subject']}

        Message:
        {validated_data['message']}
        """
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return contact_message
