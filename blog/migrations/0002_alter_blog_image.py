# Generated by Django 4.1 on 2022-08-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs/52057368932999/",
                verbose_name="main image",
            ),
        ),
    ]
