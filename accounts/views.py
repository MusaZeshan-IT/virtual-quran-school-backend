"""The views for the accounts app"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    """The view for registering a user"""

    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    """The view for logging in a user"""

    serializer_class = LoginSerializer


class LogoutView(APIView):
    """The view for logging out a user"""

    def post(self, request):
        """Handle post method for logging out"""

        refresh_token = request.data.get("refresh_token")
        if refresh_token:
            try:
                # Create a RefreshToken instance from the provided token
                token = RefreshToken(refresh_token)
                # Blacklist the refresh token
                token.blacklist()
                return Response(
                    {"message": "Logged out successfully"},
                    status=status.HTTP_205_RESET_CONTENT,
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST
        )
