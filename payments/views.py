"""The views for the payment app."""

import json
import requests
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer

JAZZCASH_API_URL = "https://www.jazzcash.com.pk/"


class OrderStatusView(viewsets.ModelViewSet):
    """The view for handling order status requests"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@csrf_exempt
def initiate_payment(request):
    """Handle payment initiation"""

    if request.method == "POST":
        data = json.loads(request.body)
        course = data.get("course")
        amount = course["fee"]

        # Define JazzCash payment initiation parameters
        payload = {
            "amount": amount,
            "merchant_id": settings.JAZZCASH_MERCHANT_ID,
            "password": settings.JAZZCASH_PASSWORD,
            "return_url": "https://virtualquranschool.netlify.app/payment-success/",  # Update with your success page URL
            "order_id": "unique_order_id",  # Replace with unique order ID
        }

        # Make request to JazzCash payment initiation endpoint
        response = requests.post(
            "https://jazzcash.com.pk/transaction/initiate", data=payload
        )

        if response.status_code == 200:
            redirect_url = response.json().get("redirect_url")
            return JsonResponse({"redirectUrl": redirect_url})
        else:
            return JsonResponse({"error": "Payment initiation failed"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def payment_callback(request):
    """Handle payment callback"""

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
