"""The models for the courses"""

from django.db import models


class Category(models.Model):
    """Model for course categories"""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    """The model for the courses"""

    name = models.CharField(max_length=100)
    hidden = models.BooleanField(default=False)
    fee = models.IntegerField()
    tutor = models.CharField(max_length=100)
    provided_by = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    enrolled = models.IntegerField(default=0, null=True, blank=True)
    duration = models.CharField(max_length=100)
    slug = models.SlugField(default="")
    type = models.CharField(max_length=100)

    class_days = models.JSONField(
        default=list, help_text="List of days of the week the course is offered"
    )
    requirements = models.JSONField(default=list, help_text="List of requirements")
    material_includes = models.JSONField(
        default=list, help_text="List of materials included in the course"
    )
    audience = models.JSONField(
        default=list, help_text="Target audience for the course"
    )
    tags = models.JSONField(
        default=list, help_text="List of tags associated with the course"
    )
    objectives = models.JSONField(
        default=list, help_text="List of learning objectives or outcomes"
    )
    brief_description = models.TextField(
        help_text="Brief description explaining who this course is for"
    )
    course_description = models.TextField(help_text="Detailed course description")
    additional_description = models.TextField(
        help_text="Additional details about the course"
    )

    categories = models.ManyToManyField(
        Category,
        related_name="courses",
        help_text="Categories associated with the course",
    )

    # Default Manager
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"
