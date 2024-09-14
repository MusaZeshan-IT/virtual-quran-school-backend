import json
import hashlib
import hmac
import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.conf import settings
from .models import Order
from .serializers import OrderSerializer

JAZZCASH_API_URL = (
    "https://sandbox.jazzcash.com.pk/ApplicationAPI/API/Payment/DoTransaction"
)


class OrderStatusView(viewsets.ModelViewSet):
    """The view for handling order status requests"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def initiate_payment(request):
    """Initiate payment and redirect the user to the JazzCash page."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = request.user
            course_name = data.get("course_name")
            amount = data.get("amount")

            if not amount or not course_name or not user:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            # Step 1: Create an order in the database
            order = Order.objects.create(
                user=user, course=course_name, status="pending", amount=amount
            )

            # Prepare JazzCash payload
            payload = {
                "pp_Version": "1.1",
                "pp_TxnType": "MWALLET",
                "pp_Language": "EN",
                "pp_MerchantID": settings.JAZZCASH_MERCHANT_ID,
                "pp_Password": settings.JAZZCASH_PASSWORD,
                "pp_TxnRefNo": str(order.id),
                "pp_Amount": str(int(amount)),
                "pp_ReturnURL": "https://virtualquranschool.netlify.app/payment-success/",
                "pp_Description": f"Payment for course: {course_name}",
                "pp_SecureHash": generate_secure_hash(order.id, amount),
            }

            # Step 3: Send request to JazzCash
            response = requests.post(JAZZCASH_API_URL, data=payload, timeout=10)

            if response.status_code == 200:
                redirect_url = response.json().get("pp_TxnRefNo")
                if redirect_url:
                    return JsonResponse({"redirectUrl": redirect_url})
                else:
                    return JsonResponse(
                        {"error": "JazzCash did not return a redirect URL"}, status=500
                    )
            else:
                return JsonResponse(
                    {"error": "Payment initiation failed with JazzCash"}, status=500
                )

        except requests.Timeout:
            return JsonResponse(
                {"error": "JazzCash payment request timed out"}, status=500
            )
        except requests.RequestException as e:
            return JsonResponse(
                {"error": f"Payment request failed: {str(e)}"}, status=500
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

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
        payment_status = request.POST.get("payment_status")
        order_id = request.POST.get("custom")  # Order ID

        if not order_id or not payment_status:
            return JsonResponse({"error": "Invalid IPN data"}, status=400)

        try:
            order = Order.objects.get(id=order_id)

            if payment_status == "Completed":
                order.status = "paid"
            elif payment_status == "Failed":
                order.status = "failed"
            elif payment_status == "Pending":
                order.status = "pending"
            else:
                order.status = "unknown"

            order.save()
            return JsonResponse({"message": "IPN processed"}, status=200)

        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)
