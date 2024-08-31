"""The urls for the blog app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="posts"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
]
