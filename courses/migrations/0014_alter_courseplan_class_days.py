# Generated by Django 5.1 on 2024-09-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0013_courseplan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseplan",
            name="class_days",
            field=models.CharField(default="Mon & Wed", max_length=100),
        ),
    ]
