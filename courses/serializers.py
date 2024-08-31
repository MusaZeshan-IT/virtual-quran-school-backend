"""The serializers for the courses app"""

from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """The serializer for the courses"""

    category = serializers.SerializerMethodField()

    class Meta:
        """The meta data for the serializer"""

        model = Course
        fields = "__all__"

    def get_category(self, obj):
        """Get the category name of the course"""
        return obj.category.name
