# Generated by Django 5.1 on 2024-09-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0018_alter_courseplan_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseplan",
            name="name",
            field=models.CharField(
                choices=[
                    ("Plan 1", "2 Days (Mon & Wed)"),
                    ("P2 Weekends", "2 Days (Sat & Sun)"),
                    ("Plan 3", "3 Days (Mon, Wed & Fri)"),
                    ("Plan 4", "5 Days (Mon to Fri)"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
    ]
