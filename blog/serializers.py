"""The serializers for the post app"""

from rest_framework import serializers
from .models import Post
from django.utils.dateformat import format


class PostSerializer(serializers.ModelSerializer):
    """The serializer for the posts"""

    comment_count = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        """The meta data for the serializer"""

        model = Post
        fields = "__all__"

    def get_comment_count(self, obj):
        """Function which counts comments"""
        return obj.comments.count()

    def get_created_at(self, obj):
        """Function which formats the created at date"""
        return format(obj.created_at, "F j, Y")  # Format as "August 23, 2024"
