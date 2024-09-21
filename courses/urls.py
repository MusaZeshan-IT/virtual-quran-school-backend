"""The urls for the courses app"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "courses/<slug:slug>/", views.CourseDetailView.as_view(), name="course-detail"
    ),
    path(
        "courses/<slug:course_slug>/plans/",
        views.CoursePlanListView.as_view(),
        name="course-plans-list",
    ),
]
