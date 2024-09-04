"""
Urls for the contact app
"""

from django.urls import path
from .views import ContactMessageCreateView

urlpatterns = [
    path("", ContactMessageCreateView.as_view(), name="contact"),
]
