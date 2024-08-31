"""The views for the blog app"""

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostList(generics.ListAPIView):
    """The post list view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    """The post detail view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
