# Generated by Django 4.2.14 on 2024-08-13 11:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_options_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
    ]