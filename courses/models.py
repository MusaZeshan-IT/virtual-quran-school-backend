"""
The models for the courses app
"""

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
    total_duration = models.CharField(max_length=100)
    class_duration = models.CharField(max_length=100, default="1 hour")
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


class CoursePlan(models.Model):
    """Model for different course plans"""

    PLAN_CHOICES = [
        ("Plan 1", "2 Days (Mon & Wed)"),
        ("Plan 2", "2 Days (Sat & Sun)"),
        ("Plan 3", "3 Days (Mon, Wed & Fri)"),
        ("Plan 4", "5 Days (Mon to Fri)"),
    ]

    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    course = models.ForeignKey(Course, related_name="plans", on_delete=models.CASCADE)
    fee = models.IntegerField()
    number_of_classes_per_week = models.IntegerField()
    class_days = models.JSONField(
        default=list, help_text="Days of the week for this plan"
    )

    # Default Manager
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} for {self.course.name}"

    def save(self, *args, **kwargs):
        """Automatically set the number of classes per week based on the plan"""
        if not self.number_of_classes_per_week:
            self.number_of_classes_per_week = len(self.class_days)
        super().save(*args, **kwargs)
