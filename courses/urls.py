"""The urls for the courses app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    path(
        "<slug:slug>/", views.CourseDetailView.as_view(), name="course-detail"
    ),
    path(
        "<slug:course_slug>/plans/",
        views.CoursePlanListView.as_view(),
        name="course-plans-list",
    ),
]
