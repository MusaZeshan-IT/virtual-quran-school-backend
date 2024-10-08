# Generated by Django 5.1 on 2024-09-02 07:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="image"
            ),
        ),
    ]
