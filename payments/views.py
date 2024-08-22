"""The views for the payment app."""

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def checkout(request):
    """Handle the checkout request."""
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")
        course = data.get("course")
        amount = data.get("amount")

        # Generate Payoneer payment URL with user details and course info
        payoneer_url = (
            f"https://payoneer.com/paymentrequest?account_id=YOUR_PAYONEER_ACCOUNT_ID&amount={amount}"
            f"&currency=USD&description=Payment for {course}&return_url=http://localhost:5173/payment-success"
        )

        # Return the Payoneer URL for redirection
        return JsonResponse({"paymentUrl": payoneer_url})

    return JsonResponse({"error": "Invalid request method."}, status=400)
