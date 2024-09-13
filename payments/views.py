"""The views for the payment app."""

import logging
import json
import hashlib
import hmac
import requests
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer

JAZZCASH_API_URL = (
    "https://sandbox.jazzcash.com.pk/ApplicationAPI/API/Payment/DoTransaction"
)

# Enable logging
logger = logging.getLogger(__name__)


class OrderStatusView(viewsets.ModelViewSet):
    """The view for handling order status requests"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@csrf_exempt
def initiate_payment(request):
    """Initiate payment and redirect the user to the JazzCash page."""
    if request.method == "POST":
        # Log the raw request body
        logger.info("Raw request body: %s", request.body)

        data = json.loads(request.body)
        user_id = data.get("user_id")  # Extract user_id
        course = data.get("course")
        amount = course["fee"]

        # Step 1: Create an order in the database
        order = Order.objects.create(user_id=user_id, status="pending", amount=amount)

        # JazzCash transaction parameters
        payload = {
            "pp_Version": "1.1",
            "pp_TxnType": "MWALLET",
            "pp_Language": "EN",
            "pp_MerchantID": settings.JAZZCASH_MERCHANT_ID,
            "pp_Password": settings.JAZZCASH_PASSWORD,
            "pp_TxnRefNo": str(order.id),  # Using the order ID
            "pp_Amount": str(int(amount * 100)),  # Amount in paisa (1 PKR = 100 paisa)
            "pp_ReturnURL": "https://virtualquranschool.netlify.app/payment-success/",
            "pp_Description": f"Payment for course: {course['name']}",
            "pp_SecureHash": generate_secure_hash(order.id, amount),
        }

        # Step 3: Send request to JazzCash
        response = requests.post(JAZZCASH_API_URL, data=payload, timeout=10)

        if response.status_code == 200:
            # Get the JazzCash URL from the response
            redirect_url = response.json().get(
                "pp_TxnRefNo"
            )  # JazzCash may send the URL
            return JsonResponse({"redirectUrl": redirect_url})
        else:
            return JsonResponse({"error": "Payment initiation failed"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


# Helper function to generate secure hash
def generate_secure_hash(order_id, amount):
    """Generate secure hash for payment request"""

    message = f"{order_id}{amount}"
    secure_hash = (
        hmac.new(
            settings.JAZZCASH_INTEGRITY_SALT.encode(), message.encode(), hashlib.sha256
        )
        .hexdigest()
        .upper()
    )
    return secure_hash


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

        except Order.objects.DoesNotExist:
            return HttpResponse("Order not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=405)
