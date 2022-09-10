# Generated by Django 4.1 on 2022-08-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0004_delete_centerslider"),
    ]

    operations = [
        migrations.CreateModel(
            name="CenterSlider",
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
                ("sequence", models.IntegerField()),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blogs/52707981070963/",
                        verbose_name="image",
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="image alt"
                    ),
                ),
            ],
            options={
                "verbose_name": "Centralized Slide",
                "verbose_name_plural": "Centralized Slides",
            },
        ),
    ]