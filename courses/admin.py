"""The admin for the courses app"""

from django.contrib import admin
from .models import Course, Category

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    """The admin for the courses"""

    list_display = (
        "name",
        "fee",
        "level",
        "enrolled",
        "duration",
        "provided_by",
        "tutor",
    )
    filter_horizontal = ('categories',)


class CategoryAdmin(admin.ModelAdmin):
    """The admin for the categories"""

    list_display = ("name",)


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
