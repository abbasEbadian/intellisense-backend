# Generated by Django 4.1 on 2022-08-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blog_author_alter_blog_corresponding_page_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs/67263329916091/",
                verbose_name="main image",
            ),
        ),
    ]
