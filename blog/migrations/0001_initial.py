# Generated by Django 4.1 on 2022-08-26 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
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
                ("title", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blogs/24019184906965/",
                        verbose_name="main image",
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="image alt"
                    ),
                ),
                ("summary", models.TextField()),
                ("content", models.TextField(verbose_name="content")),
                (
                    "estimeted_read_time",
                    models.PositiveIntegerField(
                        default=2, verbose_name="Estimeted Read Time( in minutes )"
                    ),
                ),
                (
                    "corresponding_page",
                    models.TextField(
                        choices=[
                            ("all", "All"),
                            ("forex", "Forex"),
                            ("stocks", "Stocks"),
                            ("commodities", "Commodities"),
                            ("indices", "Indices"),
                            ("etf", "ETF"),
                            ("crypto", "Crypto"),
                        ],
                        default="all",
                        max_length=15,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.blogcategory",
                        verbose_name="Category",
                    ),
                ),
            ],
        ),
    ]
