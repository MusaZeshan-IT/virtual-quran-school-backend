"""
The models for the contact app
"""

from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    """The model for the contact messages"""

    name = models.CharField(max_length=100)
    email_from = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # Default manager

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
