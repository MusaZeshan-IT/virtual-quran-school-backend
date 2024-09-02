"""The serializers for the post app"""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """The serializer for the posts"""

    comment_count = serializers.SerializerMethodField()

    class Meta:
        """The meta data for the serializer"""

        model = Post
        fields = "__all__"

    def get_comment_count(self, obj):
        """Function which counts comments"""
        return obj.comments.count()
