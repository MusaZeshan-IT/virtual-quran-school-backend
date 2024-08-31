"""The admin for the blog app"""

from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """The admin for the posts"""

    list_display = (
        "id"
        "title",
        "tags",
        "created_at",
        "slug",
    )


class CommentAdmin(admin.ModelAdmin):
    """The admin for the categories"""

    list_display = (
        "id",
        "author",
        "created_at",
        "post",
        "content",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
