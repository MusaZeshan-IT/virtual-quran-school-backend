# Generated by Django 5.1 on 2024-08-31 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(default="")),
                (
                    "tags",
                    models.JSONField(
                        default=list, help_text="List of tags associated with the post"
                    ),
                ),
                (
                    "main_description",
                    models.TextField(help_text="Main description of the post"),
                ),
                ("sub_heading_1", models.CharField(max_length=100)),
                (
                    "sub_description_1",
                    models.TextField(
                        help_text="Sub description of the post's subheading 1. This description should be in two paragraphs."
                    ),
                ),
                ("sub_heading_2", models.CharField(max_length=100)),
                (
                    "sub_description_2",
                    models.TextField(
                        help_text="Sub description of the post's subheading 2"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
    ]
