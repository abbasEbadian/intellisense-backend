# Generated by Django 4.1 on 2022-08-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs/48184896027737/",
                verbose_name="main image",
            ),
        ),
    ]