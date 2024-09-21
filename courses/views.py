"""The views for the course app"""

from rest_framework import generics
from .models import Course, CoursePlan
from .serializers import CourseSerializer, CoursePlanSerializer

# Create your views here.


class CourseList(generics.ListAPIView):
    """The post list view"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    """The course detail view"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "slug"


class CoursePlanListView(generics.ListAPIView):
    """List all plans for a course"""

    serializer_class = CoursePlanSerializer

    def get_queryset(self):
        course_slug = self.kwargs["course_slug"]
        return CoursePlan.objects.filter(course__slug=course_slug)


class CoursePlanDetailView(generics.RetrieveAPIView):
    """Retrieve a specific plan for a course"""

    serializer_class = CoursePlanSerializer

    def get_queryset(self):
        course_slug = self.kwargs["course_slug"]
        plan_id = self.kwargs["id"]
        return CoursePlan.objects.filter(course__slug=course_slug, id=plan_id)
