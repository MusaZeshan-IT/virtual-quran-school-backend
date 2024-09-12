"""The urls for the payments app"""

from django.urls import path
from . import views

urlpatterns = [
    path('payment/ipn/', views.payment_ipn, name='payment_ipn'),
]
