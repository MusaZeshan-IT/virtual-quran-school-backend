# Generated by Django 5.1 on 2024-08-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_course_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="type",
            field=models.CharField(default="normal", max_length=100),
        ),
    ]
