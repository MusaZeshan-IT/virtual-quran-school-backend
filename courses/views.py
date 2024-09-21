"""The views for the course app"""

from rest_framework import generics
from django.db.models import Prefetch
from .models import Course, CoursePlan
from .serializers import CourseSerializer, CoursePlanSerializer


class CourseListView(generics.ListAPIView):
    """List all courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    """Retrieve detailed information about a course"""

    queryset = Course.objects.all().prefetch_related(
        Prefetch("plans", queryset=CoursePlan.objects.all())
    )
    serializer_class = CourseSerializer
    lookup_field = "slug"


class CoursePlanListView(generics.ListAPIView):
    """List all plans for a specific course"""

    serializer_class = CoursePlanSerializer

    def get_queryset(self):
        course_slug = self.kwargs["course_slug"]
        return CoursePlan.objects.filter(course__slug=course_slug)
