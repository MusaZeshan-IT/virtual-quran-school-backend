# Generated by Django 5.1 on 2024-09-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0014_alter_courseplan_class_days"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseplan",
            name="fee",
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="courseplan",
            name="class_days",
            field=models.JSONField(
                default=list, help_text="Days of the week for this plan"
            ),
        ),
    ]
