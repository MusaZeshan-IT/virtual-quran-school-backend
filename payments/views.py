"""The views for the payment app."""

from django.http import HttpResponse
from .models import Order  # Assuming you have an Order model


def payment_ipn(request):
    """The view for handling IPN (Instant Payment Notification) requests"""
    if request.method == "POST":
        # Extract payment details from the request.POST (or request.body if JSON)
        payment_status = request.POST.get("payment_status")
        order_id = request.POST.get("custom")  # Assuming this is your order identifier

        try:
            # Fetch the related order
            order = Order.objects.get(id=order_id)

            # Update order status based on payment status
            if payment_status == "Completed":
                order.status = "paid"
            else:
                order.status = "pending"

            order.save()

            # Log and confirm successful IPN handling
            return HttpResponse("IPN processed", status=200)

        except Order.DoesNotExist:
            # Log or handle invalid order ID
            return HttpResponse("Order not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=405)
