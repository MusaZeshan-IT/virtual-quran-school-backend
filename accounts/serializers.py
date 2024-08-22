"""The serializers for the accounts app"""

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    """The serializer for registering a user"""

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        """The meta data for the serializer"""

        model = User
        fields = ("username", "password", "password2", "email")

    def validate(self, data):
        """Validate that the passwords match"""
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords must match.")

        username = data.get("username")
        if " " in username:
            raise serializers.ValidationError("Username cannot contain spaces.")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """The serializer for logging in a user"""

    def validate(self, attrs):
        """The validation for the login serializer"""

        # Check if the user is using an email or username
        username_or_email = attrs.get("username")
        password = attrs.get("password")

        # Try to authenticate using username
        user = User.objects.filter(username=username_or_email).first()
        if not user:
            # If no user found with username, try email
            user = User.objects.filter(email=username_or_email).first()

        # Authenticate the user
        if user:
            user = authenticate(username=user.username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        # Get or create token
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email

        return {
            "refresh": str(token),
            "access": str(token.access_token),
            "username": user.username,
        }
