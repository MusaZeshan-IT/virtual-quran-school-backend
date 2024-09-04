"""
Views for the contact app
"""

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ContactMessageSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    """
    API view to handle contact form submissions.
    """

    serializer_class = ContactMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Your message has been sent successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
