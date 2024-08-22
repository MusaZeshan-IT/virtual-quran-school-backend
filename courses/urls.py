"""The urls for the courses app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseList.as_view(), name="courses"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course-detail"),
]
