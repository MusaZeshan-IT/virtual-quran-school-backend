"""The views for the payment app."""

import requests
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Order
from .serializers import OrderSerializer

JAZZCASH_API_URL = "https://www.jazzcash.com.pk/"


class OrderStatusView(viewsets.ModelViewSet):
    """The view for handling order status requests"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def initiate_payment(request):
    """Initiate jazzcash payment"""

    # Replace these with your actual JazzCash credentials
    merchant_id = settings.JAZZCASH_MERCHANT_ID
    password = settings.JAZZCASH_PASSWORD

    # Payment initiation details
    payload = {
        "merchant_id": merchant_id,
        "password": password,
        "amount": 1000,  # Amount to be paid
        "order_id": "123456",  # Unique order ID
        "callback_url": "https://yourwebsite.com/payment/callback/",
    }

    response = requests.post(f"{JAZZCASH_API_URL}/initiate-payment", data=payload)
    return JsonResponse(response.json())


def payment_callback(request):
    # Handle payment callback
    return JsonResponse({"status": "success"})


def payment_ipn(request):
    """Handle IPN requests from the payment gateway"""
    if request.method == "POST":
        # Extract payment details from the POST data
        payment_status = request.POST.get("payment_status")
        order_id = request.POST.get("custom")  # Order ID

        if not order_id or not payment_status:
            return HttpResponse("Invalid IPN data", status=400)

        try:
            # Retrieve the order from the database
            order = Order.objects.get(id=order_id)

            # Update the order status based on the payment status
            if payment_status == "Completed":
                order.status = "paid"
            elif payment_status == "Failed":
                order.status = "failed"
            elif payment_status == "Pending":
                order.status = "pending"
            else:
                order.status = "unknown"  # Handle any unexpected statuses

            order.save()

            # Confirm that the IPN was processed successfully
            return HttpResponse("IPN processed", status=200)

        except Order.DoesNotExist:
            return HttpResponse("Order not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=405)
