"""The serializers for the courses app"""

from rest_framework import serializers
from .models import Course, CoursePlan


class CoursePlanSerializer(serializers.ModelSerializer):
    """Serializer for course plans"""

    class Meta:
        """The meta data for the serializer"""

        model = CoursePlan
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """The serializer for the courses"""

    categories = serializers.SerializerMethodField()
    plans = serializers.SerializerMethodField()

    class Meta:
        """The meta data for the serializer"""

        model = Course
        fields = "__all__"

    def get_categories(self, obj):
        """Get the category names associated with the course"""
        return [category.name for category in obj.categories.all()]

    def get_plans(self, obj):
        """Get the plans associated with the course"""
        return CoursePlanSerializer(obj.plans.all(), many=True).data
