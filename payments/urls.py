"""The urls for the payments app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
]
