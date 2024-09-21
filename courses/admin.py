"""The admin for the courses app"""

from django.contrib import admin
from .models import Course, Category, CoursePlan

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    """The admin for the courses"""

    list_display = (
        "name",
        "level",
        "type",
        "enrolled",
        "total_duration",
        "class_duration",
        "provided_by",
        "tutor",
        "hidden",
    )
    filter_horizontal = ("categories",)


class CategoryAdmin(admin.ModelAdmin):
    """The admin for the categories"""

    list_display = ("name",)


class CoursePlanAdmin(admin.ModelAdmin):
    """The admin for the course plans"""

    list_display = (
        "id",
        "name",
        "fee",
        "course",
        "number_of_classes_per_week",
        "class_days",
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePlan, CoursePlanAdmin)
admin.site.register(Category, CategoryAdmin)
