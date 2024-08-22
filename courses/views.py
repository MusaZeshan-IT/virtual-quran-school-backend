"""The views for the course app"""

from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

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
