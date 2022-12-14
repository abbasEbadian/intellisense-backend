# Generated by Django 4.1 on 2022-08-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                (
                    "title",
                    models.CharField(
                        help_text="e.g. Decentralized perpetual multi asset platform",
                        max_length=511,
                    ),
                ),
                ("sequence", models.IntegerField(help_text="sequence in the list ")),
                ("content", models.TextField()),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Show in website"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
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
        migrations.CreateModel(
            name="Util",
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
                (
                    "title",
                    models.CharField(
                        help_text="e.g. Decentralized perpetual multi asset platform",
                        max_length=255,
                    ),
                ),
                ("sequence", models.IntegerField(help_text="sequence in the list ")),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
