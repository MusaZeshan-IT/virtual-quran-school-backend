# Generated by Django 5.1 on 2024-09-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_alter_course_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="hidden",
            field=models.BooleanField(default=False),
        ),
    ]
