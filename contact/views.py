"""
Views for the contact app
"""

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactFormView(generics.CreateAPIView):
    """The view for the contact form"""

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        # Save the form data to the database
        serializer.save()

        # Extract the data
        name = serializer.validated_data.get("name")
        email_from = serializer.validated_data.get("email_from")
        subject = serializer.validated_data.get("subject")
        message = serializer.validated_data.get("message")

        # Formatting the message content
        formatted_message = f"Name: {name}\nEmail: {email_from}\n\nMessage:\n{message}"

        # Setting the email sender
        email_from_display = "Virtual Quran School <virtualquran.info@gmail.com>"

        # Compose and send the email
        send_mail(
            subject=subject,
            message=formatted_message,
            from_email=email_from_display,
            recipient_list=["virtualquran.info@gmail.com"],
            fail_silently=False,
        )

        # Return a custom response
        return Response(
            {"detail": "Message sent successfully"}, status=status.HTTP_201_CREATED
        )
