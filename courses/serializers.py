"""The serializers for the courses app"""

from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """The serializer for the courses"""

    class Meta:
        """The meta data for the serializer"""

        model = Course
        fields = "__all__"
