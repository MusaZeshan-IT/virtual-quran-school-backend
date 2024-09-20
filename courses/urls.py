"""The urls for the courses app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseList.as_view(), name="courses"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course-detail"),
    path(
        "<slug:course_slug>/plans/",
        views.CoursePlanListView.as_view(),
        name="course-plan-list",
    ),
    path(
        "plans/<int:id>/",
        views.CoursePlanDetailView.as_view(),
        name="course-plan-detail",
    ),
]
