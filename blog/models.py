"""The models for the blog app"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    """The model for the posts"""

    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="")
    tags = models.JSONField(
        default=list, help_text="List of tags associated with the post"
    )
    main_description = models.TextField(help_text="Main description of the post")
    sub_heading_1 = models.CharField(max_length=100)
    sub_description_1 = models.TextField(
        help_text="Sub description of the post's subheading 1. This description should be in two paragraphs."
    )
    sub_heading_2 = models.CharField(max_length=100)
    sub_description_2 = models.TextField(
        help_text="Sub description of the post's subheading 2"
    )

    # Default Manager
    objects = models.Manager()

    def save(self, *args, **kwargs):
        # Log before saving the image
        if self.image:
            print(f"Uploading image {self.image.name} to Cloudinary...")
            # Check if the file storage is using Cloudinary
            if isinstance(default_storage, MediaCloudinaryStorage):
                print("Cloudinary storage is being used.")
            else:
                print("Cloudinary storage is NOT being used.")

        super().save(*args, **kwargs)

        # Log after saving the image
        print(f"Image {self.image.name} uploaded successfully.")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """Model for comments on a post"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"
