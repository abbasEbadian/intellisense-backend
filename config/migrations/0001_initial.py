# Generated by Django 4.1 on 2022-08-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Roadmap",
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
                ("title", models.CharField(help_text="e.g. Phase 1", max_length=255)),
                (
                    "sequence",
                    models.IntegerField(help_text="sequence of this slide in slider "),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("done", "Done"),
                            ("ongoing", "Ongoing"),
                            ("pending", "Pending"),
                        ],
                        max_length=7,
                    ),
                ),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]