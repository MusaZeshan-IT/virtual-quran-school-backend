# Generated by Django 5.1 on 2024-09-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_short_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="short_title",
            field=models.CharField(default="short_title", max_length=100),
        ),
    ]
