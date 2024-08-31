"""The serializers for the post app"""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """The serializer for the posts"""

    class Meta:
        """The meta data for the serializer"""

        model = Post
        fields = "__all__"
