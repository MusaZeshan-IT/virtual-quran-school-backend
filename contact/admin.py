"""
The admin for the contact app
"""

from django.contrib import admin
from .models import ContactMessage

# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    """The admin for the contact messages"""

    list_display = ("name", "email_from", "subject", "created_at")


admin.site.register(ContactMessage, ContactMessageAdmin)
